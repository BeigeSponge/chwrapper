from setuptools import setup, find_packages


def readme():
    with open("README.md", encoding="utf-8") as f:
        return f.read()


setup(
    name="chwrapper",
    version="0.3.2",
    description="A simple wrapper around the Companies House API",
    long_description=readme(),
    url="https://github.com/BeigeSponge/chwrapper/archive/development.zip",
    author="James Gardiner",
    author_email="jamesg87@me.com",
    license="MIT",
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        "cookies",
        "coverage",
        "py",
        "pytest",
        "pytest-cov",
        "requests",
        "responses",
        "wheel",
    ],
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
)
