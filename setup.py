from setuptools import setup
from setuptools import find_packages

# with open('README.rst') as file:
#     long_description = file.read()

setup(
  name = 'datagod',
  packages = find_packages(),
  version = '0.2.2',
  description = 'A library focused on faking data',
  author = 'gaocegege',
  author_email = 'gaocegege@hotmail.com',
  url = 'https://github.com/gaocegege/Data-God', # use the URL to the github repo
  download_url = 'https://github.com/gaocegege/Data-God/tarball/0.2.2', # I'll explain this in a second
  keywords = ['graph', 'data'], # arbitrary keywords
  classifiers = [],
  install_requires = ['scipy', 'numpy', 'matplotlib'],
  # long_description=long_description,
  license='MIT',
)