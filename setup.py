from setuptools import setup, find_packages

setup(
    name="tinymodel",
    version="0.1.0",
    packages=find_packages(),
    author="Juan Olano",
    author_email="jcolano@teams.us",
    description="A small model for AI completions",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jcolano/tinymodel",
    install_requires=[
        "httpx>=0.20.0",
        # Add other dependencies if any
    ],
    python_requires='>=3.6',
    # Other optional fields
)
