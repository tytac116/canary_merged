import codecs
import os.path
from setuptools import setup, find_namespace_packages, find_packages
from opencanary_correlator import __version__
import sys

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    """
    Reading the package version dynamically.
    https://packaging.python.org/en/latest/guides/single-sourcing-package-version/
    """
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

requirements = [
    'Twisted',
    'pyasn1',
    'cryptography',
    'simplejson',
    'requests',
    'zope.interface',
    'PyPDF2',
    'fpdf',
    'passlib',
    'Jinja2',
    'ntlmlib',
    'bcrypt',
    'setuptools',
    'hpfeeds',
    'cffi',
    'docopt',
    'httplib2',
    'mandrill',
    'pycparser',
    'pyparsing',
    'PyNaCl',
    'pytz',
    'redis',
    'six',
    'twilio',
    'wheel',]


setup(
    name='opencanary',
    version=get_version("opencanary/__init__.py"),
    url='http://www.thinkst.com/',
    author='Thinkst Applied Research',
    author_email='info@thinkst.com',
    description='OpenCanary daemon',
    long_description='A low interaction honeypot intended to be run on internal networks.',
    install_requires=requirements,
    license='BSD',
    packages=find_namespace_packages(
        exclude=[
            'docs','docs*'
            'opencanary.test','opencanary.test*'
        ]
    ),
    include_package_data = True,
    scripts=['bin/opencanaryd','bin/opencanary.tac','bin/opencanary-correlator'], #added script for correlator 
    platforms='any',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Framework :: Twisted",
        "Topic :: System :: Networking",
        "Topic :: Security",
        "Topic :: System :: Networking :: Monitoring",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Operating System :: POSIX :: Linux",
        "Operating System :: POSIX :: BSD :: FreeBSD",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: BSD License",
    ],
)
