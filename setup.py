# Based on STScI's JWST calibration pipeline.

from __future__ import print_function

import os
import subprocess
import sys
from setuptools import setup, find_packages, Extension, Command
from glob import glob

# Open the README as the package long description
readme = open('README.rst', 'r')
README_TEXT = readme.read()
readme.close()


NAME = 'nifty4gemini'
SCRIPTS = glob('scripts/*')
PACKAGE_DATA = {
    '': ['*.dat', '*.cfg', '*.fits', '*.txt']
}

setup(
    name=NAME,
    version="1.0.1",
    author='mbusserolle',
    author_email='mbussero@gemini.edu',
    description='Gemini Instruments Data Reduction Framework.',
    long_description = README_TEXT,
    url='http://www.gemini.edu',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: MacOS X',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Scientific/Engineering :: Physics',
    ],
    keywords='Gemini NIFS nifs pipeline reduction data IRAF iraf PYRAF pyraf astronomy integral field spectroscopy ifs ifu',
    python_requires='~=2.7',
    scripts=SCRIPTS, # TODO(nat): Update this to use entry_points instead of scripts for better cross-platform performance
    packages=find_packages(),
    package_data=PACKAGE_DATA
)
