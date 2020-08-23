<p align="center">
  <img src="https://i.imgur.com/o5qAbVt.png" alt="DuckPy" height="250px">
  <h4 align="center">A simple Python module for searching on DuckDuckGo.</h4>
</p>

![PyPI](https://img.shields.io/pypi/v/duckpy) ![GitHub](https://img.shields.io/github/license/AmanoTeam/duckpy)


## Installation

#### Duckpy can be installed using pip with this command

```bash
pip install -U duckpy
```

#### Alternatively, you can install the most recent version from git

```bash
pip install -U git+https://github.com/AmanoTeam/duckpy
```

#### If you are using Debian, you can install with this command (Currently only in Debian Unstable)

```bash
sudo apt install python3-duckpy
```

## Usage

```python
from duckpy import Client

client = Client()

results = client.search("Python Wikipedia")

# Prints first result title
print(results[0]["title"])

# Prints first result URL
print(results[0]["url"])

# Prints first result description
print(results[0]["description"])
```

### We also provide an asynchronous version inside the `AsyncClient` class


```python
import asyncio
from duckpy import AsyncClient

client = AsyncClient()

async def get_results():
  results = await client.search("Python Wikipedia")

  # Prints first result title
  print(results[0]["title"])

  # Prints first result URL
  print(results[0]["url"])

  # Prints first result description
  print(results[0]["description"])


loop = asyncio.get_event_loop()
loop.run_until_complete(get_results())
```

### The result

```
Python (programming language) - Wikipedia
https://en.wikipedia.org/wiki/Python_(programming_language)
Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991...
```


## Advanced usage

You can also set up proxies or set up custom User-Agent strings depending on your needs.

### Setting up proxies

DuckDuckGo may temporarily block your request IP or return empty results, especially if you are using the library for scraping, bots and other stuff that generate many requests. This is not a duckpy issue and can be prevented using proxies.

You can pass a list with proxies in the Client object, then duckpy will use these proxies to make requests:

```python
import duckpy

client = duckpy.Client(proxies=['http://123.45.67.89:80', 'https://98.76.54.32:443'])
```

If you pass more than one proxy, they will be randomly chosen every time you use the .search() method.

### Setting up custom User-Agents

```python
import duckpy

user_agents = [
  "Mozilla/5.0 (X11; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0",
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
]

client = duckpy.Client(default_user_agents=user_agents)
```

Again, if you pass more than one User-Agent, they will be randomly chosen every time you use the .search() method.

## Disclaimer

We are not affiliated, associated, authorized, endorsed by, or in any way officially connected with DuckDuckGo, or any of its subsidiaries or its affiliates. The official DuckDuckGo website can be found at https://duckduckgo.com.
