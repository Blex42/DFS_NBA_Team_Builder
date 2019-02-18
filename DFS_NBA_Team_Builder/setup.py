import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DFSNBA_TeamBuilder",
    version="0.0.2",
    author="Blex42",
    author_email="blextechguides@gmail.com",
    description="This package is used for creating draftkings lineups",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Blex42/DFS_NBA_Team_Builder",
    packages=setuptools.find_packages(),
    install_requires=[
          'pandas','numpy','PuLP'
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)