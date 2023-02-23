import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-rolldice",
    version="0.4.1",
    author="Finian Blackett",
    author_email="spamsuckersunited@gmail.com",
    description="A module for parsing dice notation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ThePlasmaRailgun/py-rolldice",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ),
    install_requires=[
        "regex",
    ],
)
