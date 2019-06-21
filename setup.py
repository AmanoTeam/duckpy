import setuptools

with open('README.md') as f:
    readme = f.read()

setuptools.setup(
    name='duckpy',
    version='2.0.0',

    packages=['duckpy', 'duckpy.aio'],
    install_requires=['bs4', 'urllib3', 'aiohttp', 'certifi'],

    url='https://github.com/AmanoTeam/duckpy',

    author='Amano Team',
    author_email='contact@amanoteam.ml',

    license='MIT',

    description='A simple module for searching on DuckDuckGo',
    long_description=readme,
    long_description_content_type='text/markdown'
)
