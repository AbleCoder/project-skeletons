#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

# support setuptools or distutils
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# import ourselves for version info
import PROJECT


PATH = os.path.dirname(__file__)

packages = [
    'PROJECT',
]

requires = [
    #"requests==1.0.0", # example
]

scripts = [
    #'bin/example-one.py',
    #'bin/example-two.py',
]

setup(
    name='PROJECT',
    version=PROJECT.__version__,
    author='AbleCoder',
    author_email='coder@able.cd',
    license='LICENSE.txt',
    description='PROJECT Desc',
    long_description=open(os.path.join(PATH, 'README.rst')).read() + '\n\n' +
                     open(os.path.join(PATH, 'HISTORY.rst')).read(),
    url='http://github.com/AbleCoder/PROJECT',
    download_url='http://github.com/AbleCoder/PROJECT/tarball/master',
    packages=packages,
    install_requires=requires,

    # List of Classifiers:
    #   https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console"
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Topic :: Utilities",
    ],
)
