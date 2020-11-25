#!/usr/bin/env python

from setuptools import setup, find_packages
from tasks import version_info, write_version_py

# write version on the fly - inspired by numpy
MAJOR = 0
MINOR = 0
MICRO = 0

# Version module
write_version_py((MAJOR, MINOR, MICRO))


# README into long description
with open("README.md") as f:
    readme = f.read()
    print(readme)

setup(
    name="opale",
    version=version_info(MAJOR, MINOR, MICRO),
    description="Dark theme based on Alabaster",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Alessandro Candido",
    author_email="candido.ale@gmail.com",
    url="",
    package_dir={"": "src"},
    packages=find_packages("src"),
    include_package_data=True,
    entry_points={"sphinx.html_themes": ["opale = opale"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Documentation",
        "Topic :: Software Development :: Documentation",
    ],
)
