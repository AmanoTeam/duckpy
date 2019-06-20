import setuptools

with open('README.md') as f:
    readme = f.read()

setuptools.setup(
    name='duckpy',
    version='1.2.3',

    packages=['duckpy'],
    install_requires=['bs4', 'urllib3', 'certifi'],

    url='https://github.com/AmanoTeam/duckpy',

    author='Amano Team',
    author_email='contact@amanoteam.ml',

    license='MIT',

    description='A simple module that searches on DuckDuckGo',
    long_description=readme,
    long_description_content_type='text/markdown'
)
