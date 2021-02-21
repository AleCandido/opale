#!/usr/bin/env python
import sys
import pathlib

from setuptools import setup, find_packages
import packutil as pack

repo_path = pathlib.Path(__file__).parent

# fmt: off
sys.path.insert(0, str(repo_path.absolute()))
import utils
sys.path.pop(0)
# fmt: on

# write version on the fly - inspired by numpy
MAJOR = 0
MINOR = 1
MICRO = 0


def setup_package():
    utils.build_theme.all()

    # README into long description
    with open("README.md") as f:
        readme = f.read()
        print(readme)

    # write version
    pack.versions.write_version_py(
        MAJOR,
        MINOR,
        MICRO,
        pack.versions.is_released(repo_path),
        filename="src/opale/version.py",
    )

    setup(
        name="opale",
        version=pack.versions.mkversion(MAJOR, MINOR, MICRO),
        description="Dark theme based on Alabaster",
        long_description=readme,
        long_description_content_type="text/markdown",
        author="Alessandro Candido",
        author_email="candido.ale@gmail.com",
        url="",
        package_dir={"": "src"},
        packages=find_packages("src"),
        include_package_data=True,
        package_data={
            "": ["LICENSE", "README.md"],
            "opale": ["src/opale/*.html", "src/opale/theme.conf", "src/opale/static/*"],
        },
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


if __name__ == "__main__":
    setup_package()
