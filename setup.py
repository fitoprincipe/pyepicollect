#!/usr/bin/env python

import os
from setuptools import setup, find_packages
from pyepicollect import __version__


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

# the setup
setup(
    name='pyepicollect',
    version=__version__,
    description='Read EpiCollect 5 data from python',
    long_description=read('README.md'),
    url='',
    author='Rodrigo E. Principe',
    author_email='fitoprincipe82@gmail.com',
    license='',
    keywords='epicollect epicollect5 database',
    packages=find_packages(exclude=('docs', 'js')),
    include_package_data=True,
    install_requires=['requests'],
    extras_require={
        'dev': [],
        'docs': [],
        'testing': ['pytest>=4.2.1'],
    },
    classifiers=['Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.6'],
)