try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Lexicon generation project',
	'author': 'Samir Aryamane',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it',
	'author_email': 'samirarya@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['lexicon'],
	'scripts': [],
	'name': 'lexicon'
}

setup(**config)