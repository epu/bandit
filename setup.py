# https://setuptools.readthedocs.io/en/latest/setuptools.html#installing-setuptools
from setuptools import setup, find_packages

setup(
	name='bandit',
	version='0.1',
	packages=find_packages(),
	description='bandit coverband generator, a twitter bot',
	author='Erik Purins',
	author_email='erik@purins.com',
	url='https://github.com/epu/bandit',
    install_requires=['twitter>=1.17.1'],
)