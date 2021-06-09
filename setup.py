# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in remove_help_menu/__init__.py
from remove_help_menu import __version__ as version

setup(
	name='remove_help_menu',
	version=version,
	description='remove help from navigation menu',
	author='VTBS',
	author_email='vtbs@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
