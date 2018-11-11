import setuptools

with open('README.md') as f:
    readme = f.read()

setuptools.setup(
    name='duckpy',
    version='1.1.0',
    packages=setuptools.find_packages(),
    url='https://github.com/AmanoTeam/duckpy',
    author='Amano Team',
    author_email='contact@amanoteam.ml',
    description='A simple module that searches on DuckDuckGo',
    long_description=readme,
    long_description_content_type='text/markdown'
)
