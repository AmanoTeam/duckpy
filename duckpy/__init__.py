import random
import secrets
import certifi
import urllib3
from urllib.parse import unquote
from bs4 import BeautifulSoup


ddg_url = 'https://duckduckgo.com/html'


class Client:
    def __init__(self, proxies=None, random_ua=True):
        if isinstance(proxies, type(None)):
            self.proxies = None
        elif isinstance(proxies, str):
            self.proxies = [proxies]
        elif isinstance(proxies, list):
            self.proxies = proxies

        self.http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())

        self.random_ua = random_ua

    def search(self, query, exact_match=False, **kwargs):
        if exact_match:
            query = '"%s"' % query
        if self.proxies:
            proxy = random.choice(self.proxies)
            http = urllib3.ProxyManager(proxy)
        else:
            http = self.http
        headers = {'User-Agent': secrets.token_hex(5) + '/1.0'} if self.random_ua else None

        r = http.request('GET', ddg_url, fields=dict(q=query, **kwargs), headers=headers)

        return parse_page(r.data)


def parse_page(html):
    soup = BeautifulSoup(html, "html.parser")
    results = []
    for i in soup.find_all('div', {'class': 'links_main'}):
        try:
            title = i.h2.a.text
            description = i.find('a', {'class': 'result__snippet'}).text
            url = i.find('a', {'class': 'result__url'}).get('href')
            results.append(dict(title=title, description=description, url=unquote(url[15:])))
        except AttributeError:
            pass
    return results
