#!/usr/bin/env python

from setuptools import setup
from mf2py import VERSION

setup(name='mf2py',
      version=VERSION,
      description='Python Microformats2 parser',
      author='Tom Morris',
      author_email='tom@tommorris.org',
      url='http://microformats.org/wiki/mf2py',
      install_requires=['html5lib', 'requests', 'BeautifulSoup4'],
      tests_require=['nose', 'mock'],
      packages=['mf2py'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Topic :: Text Processing :: Markup :: HTML'
      ])
