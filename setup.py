from setuptools import setup, find_packages

"""
helps to import modules from parent folder!
used when I want to decorate(to calculate time) function in src.http.client
from utility.utils
"""
setup(name='fileTransferProtocolsProject',
      version='1.0',
      packages=find_packages()
      )