#!/usr/bin/env python

"""Octopus packaging instructions."""

from setuptools import setup, find_packages
from agile import __version__, __author__, __project__, __teaser__

REQUIREMENTS = [
    'jira',
    'github3.py',
    'influxdb',
    'click',
    'PyYaml'
]


def long_description():
    """Insert readme.md into the package."""
    try:
        with open('readme.md') as readme_fd:
            return readme_fd.read()
    except IOError:
        return 'failed to read readme.md'


setup(
    name=__project__,
    version=__version__,
    description=__teaser__,
    author=__author__,
    author_email='xavier.bruhiere@gmail.com',
    packages=find_packages(),
    long_description=long_description(),
    entry_points={
        'console_scripts': [
            'agile = agile.__main__:main',
        ],
    },
    install_requires=REQUIREMENTS
)
