try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

config = {
  'description': 'Python server for creating accounts',
  'author': 'Rob Layton',
  'url': 'https://github.com/roblayton/pyaccounts',
  'download_url': 'Download link',
  'author_email': 'hire@roblayton.com',
  'version': '0.1.0',
  'install_requires': ['pytest'], #dependencies
  'packages': [],
  'scripts': [],
  'name': 'pyaccounts'
}

setup(**config)
