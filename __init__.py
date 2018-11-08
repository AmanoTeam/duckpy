import requests
from urllib.parse import unquote
from bs4 import BeautifulSoup


def search(query, **kwargs):
	r = requests.get('https://duckduckgo.com/html', params=dict(q=query, **kwargs))
	soup = BeautifulSoup(r.text, "html.parser")
	results = []
	for i in soup.find_all('div', {'class': 'links_main'}):
		try:
			title = i.h2.a.text
			description = i.find('a', {'class': 'result__snippet'}).text
			url = i.find('a', {'class': 'result__url'}).get('href')
			results.append(dict(title=title, description=description, url=unquote(url[15:])))
		except AttributeError:   #It's normal this bug.
			pass

	return dict(results=results)
