<h6 align="center">
  <img src="https://i.imgur.com/WyjAm8t.png" alt="DuckPy" height="250px">
  <h5 align="center">A simple Python module that searches on DuckDuckGo.</h5>
</h6>


## How to use It?
To use DuckPy is easy, let's start:

### First example:

```python
import duckpy

search = duckpy.search("test")

# Prints first result title
print(search["results"][0]["title"])

# Prints first result URL
print(search["results"][0]["url"])

# Prints first result description
print(search["results"][0]["description"])
```
The result will be like this:
```
Find online tests, practice test, and test creation software ...
https://www.test.com/
Online tests and testing for certification, practice tests, test making tools, medical testing and more.
```
