<h6 align="center">
  <img src="https://i.imgur.com/o5qAbVt.png" alt="DuckPy" height="250px">
  <h5 align="center">A simple Python module for searching on DuckDuckGo.</h5>
</h6>


## Installation

Duckpy can be installed using pip with this command:

```bash
pip install -U duckpy
```

#### Alternatively, you can install directly from git:

```bash
pip install -U git+https://github.com/AmanoTeam/duckpy
```

## Usage:

To use duckpy is easy, let's see some examples:

### First example:

```python
import duckpy

client = duckpy.Client()

search = client.search("Amano Team duckpy")

# Prints first result title
print(search[0]["title"])

# Prints first result URL
print(search[0]["url"])

# Prints first result description
print(search[0]["description"])
```

We also provide an asynchronous version:


```python
import asyncio
import duckpy.aio

client = duckpy.aio.Client()

async def get_results():
  search = await client.search("Amano Team duckpy")

  # Prints first result title
  print(search[0]["title"])

  # Prints first result URL
  print(search[0]["url"])

  # Prints first result description
  print(search[0]["description"])


loop = asyncio.get_event_loop()
loop.run_until_complete(get_results())
```

The result:

```
GitHub - AmanoTeam/duckpy: A simple Python module that ...
https://github.com/AmanoTeam/duckpy
A simple Python module for searching on DuckDuckGo - AmanoTeam/duckpy
```


# Advanced usage:

You can also set up proxies and/or enable or disable random User-Agents depending on your needs.

## Setting up proxies:

You can pass a list with proxies in the Client object, then duckpy will use these proxies to make requests.

#### Example:

```python
import duckpy

client = duckpy.Client(proxies=['123.45.67.89:80', '98.76.54.32:443'])
```

If you pass more than one proxy, them will be randomly chosen every time you use the .search() method.
