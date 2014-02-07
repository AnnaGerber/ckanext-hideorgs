from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(
	name='ckanext-hideorgs',
	version=version,
	description="A CKAN 2 plugin that hides the organizations feature from the web interface",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Anna Gerber',
	author_email='',
	url='',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.hideorgs'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
        [ckan.plugins]
	# Add plugins here, eg
    hideorgs=ckanext.hideorgs.plugin:HideOrgsPlugin
	""",
)
