"""
    dwm package setup
"""

from __future__ import print_function
from setuptools import setup, find_packages

__version__ = '1.1.0'

def readme():
    """ open readme for long_description """

    try:
        with open('README.md') as fle:
            return fle.read()
    except IOError:
        return ''

setup(
    name='dwm',
    version=__version__,
    url='https://github.com/rh-marketingops/dwm',
    license='GNU General Public License',
    author='Jeremiah Coleman',
    tests_require=['nose', 'mongomock>=3.5.0'],
    install_requires=['pymongo>=3.2.2', 'tqdm>=4.8.4'],
    author_email='colemanja91@gmail.com',
    description='Best practices for marketing data quality management',
    long_description=readme(),
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    test_suite='nose.collector',
    classifiers=[
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
    keywords='marketing automation data quality cleanse washing cleaning'
)
