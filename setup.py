try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'My Name',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.0.0',
    'install_requires': [],
    'packages': ['people_tracker'],
    'scripts': [],
    'name': 'people_tracker'
}

setup(**config)
