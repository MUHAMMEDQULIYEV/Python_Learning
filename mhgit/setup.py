from setuptools import setup

setup(
    name="mhgit",
    version="1.0",
    packages=["mhgit"],
    entry_points={"console_scripts": ["mhgit=mhgit.cli:main"]},
)
