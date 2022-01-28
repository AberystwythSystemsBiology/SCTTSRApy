import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name = "scttsrapy",
    version = "0.0.1",
    author = "Keiron O'Shea",
    author_email = "keiron@fastmail.co.uk",
    description = ("A Python Interface to the SNOWSTORM SNOMED-CT API."),
    license = "GPLv3",
    keywords = "snomed-ct snowstorm",
    url = "https://github.com/AberystwythSystemsBiology/SCTTSRApy",
    packages=['scttsrapy'],
    install_requires=required,
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)