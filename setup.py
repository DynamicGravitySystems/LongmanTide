# -*- coding: utf-8 -*-

import os
from setuptools import setup

__version__ = '0.4.0-beta.1'
requirements = [
    'numpy == 1.18.5',
    'pandas == 1.0.4'
]


def join_relpath(file):
    return os.path.join(os.path.dirname(__file__), file)


with open(join_relpath('LICENSE'), 'r') as fd:
    _license = fd.read().strip()

with open(join_relpath('README.rst'), 'r') as fd:
    long_description = fd.read().strip()

setup(
    name='tidegravity',
    version=__version__,
    packages=['tidegravity'],
    install_requires=requirements,
    extras_require={
        'MPL': ['matplotlib>=2.2.0']
    },
    tests_require=['pytest'],
    python_requires='>=3.5.*',
    description="Tide gravitational correction based on I.M. Longman's Formulas for "
                "Computing the Tidal Accelerations Due to the Moon and the Sun",
    author='Zachery P. Brady, John R. Leeman',
    author_email='bradyzp@dynamicgravitysystems.com',
    url='https://github.com/bradyzp/LongmanTide/',
    download_url='https://github.com/bradyzp/LongmanTide',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Microsoft',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Software Development :: Libraries',
    ],
    long_description=long_description,
)
