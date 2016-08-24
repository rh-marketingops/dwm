from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import codecs
import os
import sys

import dwm
#
# def readme():
#     with open('README.md') as f:
#         return f.read()

setup(
    name='dwm',
    version=dwm.__version__,
    url='https://github.com/rh-marketingops/dwm',
    license='GNU General Public License',
    author='Jeremiah Coleman',
    tests_require=['nose', 'mongomock>=3.5.0'],
    install_requires=['pymongo>=3.2.2', 'tqdm>=4.8.4'],
    author_email='colemanja91@gmail.com',
    description='Best practices for marketing data quality management',
    #long_description=readme(),
    packages=['dwm'],
    include_package_data=True,
    platforms='any',
    test_suite = 'nose.collector',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks'
        ],
    keywords = 'marketing automation data quality cleanse washing cleaning'
)
