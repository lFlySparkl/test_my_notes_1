#work1
from setuptools import setup, find_namespace_packages

setup(name = "bh",
      version = "0.99.88",
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['bh = hw_12.hw12:main']})