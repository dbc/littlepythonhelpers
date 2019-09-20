import pathlib
from setuptools import setup

# Get path to current directory.
here = pathlib.Path(__file__).parent

# Get the README
readme = (here / "README.rst").read_text()

with open (here.joinpath( 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='littlepythonhelpers',
    version ='1.2',
    description = 'Personal collection of small, handy Python snippets.',
    long_description = long_description,
    long_description_content_type = 'text/x-rst',
    py_modules=['littlepythonhelpers'],
)

