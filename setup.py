# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='antsibull-docs-parser',
    version='1.0.0',
    description='Python library for processing Ansible documentation markup',
    author_email='Felix Fontein <felix@fontein.de>',
    maintainer_email='Felix Fontein <felix@fontein.de>, Maxwell G <maxwell@gtmx.me>',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Ansible',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Typing :: Typed',
    ],
    extras_require={
        'codeqa': [
            'antsibull-changelog',
            'flake8',
            'pylint',
            'reuse',
        ],
        'coverage': [
            'coverage[toml]',
        ],
        'dev': [
            'antsibull-docs-parser[codeqa]',
            'antsibull-docs-parser[coverage]',
            'antsibull-docs-parser[formatters]',
            'antsibull-docs-parser[test]',
            'antsibull-docs-parser[typing]',
            'nox',
        ],
        'formatters': [
            'black',
            'isort',
        ],
        'test': [
            'pytest',
            'pytest-cov',
            'pytest-error-for-skips',
            'pyyaml',
        ],
        'typing': [
            'mypy',
            'pyre-check>=0.9.17',
        ],
    },
    packages=[
        'antsibull_docs_parser',
    ],
    package_dir={'': 'src'},
)
