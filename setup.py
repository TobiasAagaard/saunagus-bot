from setuptools import setup, find_packages

setup(
    name="bookbot",
    version="1.0.0",
    author="Tobias Aagaard Christiansen",
    description= "A command-line tool for analyzing book files and generating statistics.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    py_modules=["main", "stats"],
    entry_points={
        "console_scripts": [
            "bookbot = main:main",
        ],    
    },
    python_requires=">=3.6",

)