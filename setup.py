try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
version = '0.1.8'
setup(
    name = 'diffimg',
    packages = ['diffimg'], # this must be the same as the name above
    version = version,
    description = 'Get the % difference in images + generate a diff image',
    author = 'Nicolas Hahn',
    author_email = 'nicolas@stonespring.org',
    url = 'https://github.com/nicolashahn/python-image-diff',
    download_url = 'https://github.com/nicolashahn/python-image-diff/archive/v{}.tar.gz'.format(version),
    keywords = ['diff', 'difference', 'image'],
    classifiers = [],
    install_requires = ['Pillow>=4.3'],
)
