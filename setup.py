from setuptools import setup, find_packages

setup(name='protopost',
  version='0.0.0',
  install_requires = [
    "flask",
    "flask_restful",
    "requests"
  ],
  packages=find_packages())
