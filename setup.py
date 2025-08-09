from setuptools import setup, find_packages
# find_packages() automatically discovers all packages and subpackages. whatever folder there is __init__ file, that folder will be considered as a package.


setup(
    name="document_portal",
    author="Onkar Shelar",
    version="0.1",
    packages=find_packages(),
)

# pip install -e .  # to install the package in editable mode.
# pip install -e .[dev]  # to install the package with dev dependencies.
# pip install -e .[dev,prod]  # to install the package with both dev and prod dependencies.
# pip install -e .[dev,prod,extra]  # to install the package with dev, prod and extra dependencies.

# it will create .egg-info folder in the current directory, which contains the metadata about the package.
# when we run pip list, we will see the package name and version and location of the package.
# when we run pip uninstall document_portal, it will uninstall the package.
# LangChain, LangGraph, pandas are projects which are created by dev as a package and then we consume it as a package
#  we can host our package in PyPI (Python Package Index) or any other package index.
