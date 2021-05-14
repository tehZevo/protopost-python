from setuptools import setup, find_packages

setup(name='protopost',
  version='0.0.0',
  install_requires = [
    "flask==1.1.2",
    "flask_restful",
    "requests"
  ],
  packages=find_packages())
