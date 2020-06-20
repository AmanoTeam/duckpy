import random
import secrets
import certifi
import aiohttp
from typing import Union
from .. import parse_page, ddg_url
from urllib.parse import unquote
from bs4 import BeautifulSoup


class Client:
    def __init__(self, proxies: Union[int, str] = None, random_ua: bool = True):
        if isinstance(proxies, type(None)):
            self.proxies = None
        elif isinstance(proxies, str):
            self.proxies = [proxies]
        elif isinstance(proxies, list):
            self.proxies = proxies

        self.random_ua = random_ua

    async def search(self, query: str, exact_match: bool = False, **kwargs):
        if exact_match:
            query = '"%s"' % query
        proxy = random.choice(self.proxies) if self.proxies else None
        headers = {'User-Agent': secrets.token_hex(5) + '/1.0'} if self.random_ua else None

        async with aiohttp.ClientSession() as session:
            r = await session.get(ddg_url, proxy=proxy, params=dict(q=query, **kwargs), headers=headers)
            data = await r.read()

        return parse_page(data)
