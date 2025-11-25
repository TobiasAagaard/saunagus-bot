from setuptools import setup, find_packages

setup(
    name="bookbot",
    version="1.0.0",
    author="Tobias Aagaard Christiansen",
    description="A command-line tool for analyzing book files and generating statistics.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/TobiasAagaard/bookbot",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "bookbot=bookbot.main:main",
        ],
    },
    python_requires=">=3.6",
)