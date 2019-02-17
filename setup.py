import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DFS_NBA_Team_Builder-Blex42",
    version="0.0.1",
    author="Blex42",
    author_email="blextechguides@gmail.com",
    description="This package is used for created draftkings lineups",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows 10",
    ],
)