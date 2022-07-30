from setuptools import setup, find_packages

setup(name='protopost',
  version='0.0.0',
  install_requires = [
    "flask>=2",
    "flask_restful",
    "flask_cors",
    "requests"
  ],
  packages=find_packages())
