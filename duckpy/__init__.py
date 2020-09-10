import asyncio
import random
import httpx
from .types import ResultDict
from typing import List
from warnings import warn
from typing import Union
from bs4 import BeautifulSoup


ddg_url = 'https://html.duckduckgo.com/html'


class BaseClient:
    def __init__(self, proxies: Union[list, str] = None, default_user_agents: Union[list, str] = None, random_ua: bool = None):
        if random_ua is not None:
            warn("The random_ua parameter has been deprecated in favor of the default_user_agents parameter and will be removed in a future release.", DeprecationWarning, 2)

        self.proxies = proxies
        self.default_user_agents = default_user_agents


class Client(BaseClient):
    def search(self, query: str, exact_match: bool = False, **kwargs) -> List[ResultDict]:
        if exact_match:
            query = '"%s"' % query

        if isinstance(self.proxies, str):
            proxy = self.proxies
        elif isinstance(self.proxies, list):
            proxy = random.choice(self.proxies) if self.proxies else None
        else:
            proxy = None
        if isinstance(self.default_user_agents, str):
            ua = self.default_user_agents
        elif isinstance(self.default_user_agents, list):
            ua = random.choice(self.default_user_agents) if self.default_user_agents else None
        else:
            ua = None
        headers = {'User-Agent': ua} if ua else None

        with httpx.Client(proxies=proxy, http2=True) as http:
            r = http.post(ddg_url, data=dict(q=query, **kwargs), headers=headers)
            data = r.read()

            return parse_page(data)


class AsyncClient(BaseClient):
    def __init__(self, proxies: Union[list, str] = None, default_user_agents: Union[list, str] = None, random_ua: bool = None):
        self.loop = asyncio.get_event_loop()
        super().__init__(proxies=proxies, default_user_agents=default_user_agents, random_ua=random_ua)

    async def search(self, query: str, exact_match: bool = False, **kwargs) -> List[ResultDict]:
        if exact_match:
            query = '"%s"' % query

        if isinstance(self.proxies, str):
            proxy = self.proxies
        elif isinstance(self.proxies, list):
            proxy = random.choice(self.proxies) if self.proxies else None
        else:
            proxy = None
        if isinstance(self.default_user_agents, str):
            ua = self.default_user_agents
        elif isinstance(self.default_user_agents, list):
            ua = random.choice(self.default_user_agents) if self.default_user_agents else None
        else:
            ua = None
        headers = {'User-Agent': ua} if ua else None

        async with httpx.AsyncClient(proxies=proxy, http2=True) as http:
            r = await http.post(ddg_url, data=dict(q=query, **kwargs), headers=headers)
            data = r.read()

            return await self.loop.run_in_executor(None, parse_page, data)


def parse_page(html: Union[str, bytes]) -> List[ResultDict]:
    soup = BeautifulSoup(html, "html.parser")
    results = []
    for i in soup.find_all('div', {'class': 'links_main'}):
        if i.find('a', {'class': 'badge--ad'}):
            continue
        try:
            title = i.h2.a.text
            description = i.find('a', {'class': 'result__snippet'}).text
            url = i.find('a', {'class': 'result__url'}).get('href')
            results.append(ResultDict(title=title, description=description, url=url))
        except AttributeError:
            pass
    return results
