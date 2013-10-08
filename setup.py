#!/usr/bin/env python

import os
import sys
import multiprocessing  # NOQA

from setuptools import setup, find_packages

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))


def read(fname):
    return open(fname).read()


install_requires = [
    'flask==0.10.1',
]

test_requires = [
    'mock==1.0.1',
    'tox==1.4.3',
    'nose==1.3',
    'coverage==3.6',
    'coveralls==0.2',
]

dev_requires = test_requires + [
    'pytest==2.3.5',
    'pdbpp==0.7',
    'ipython==0.13.2',
    'flake8==2.0',
]

setup(
    name='foo',
    version='0.0.1',
    author='Christopher John Reeves',
    author_email='chris@adaptivelab.co.uk',
    url='https://github.com/krak3n/foo.git',
    description='Fooythings',
    long_description='foo',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    test_suite='runtests.runtests',
    extras_require={
        'test': test_requires,
        'develop': dev_requires,
    },
    classifiers=[
        'Environment :: Console',
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Operating System :: Unix',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    license='BSD'
)
