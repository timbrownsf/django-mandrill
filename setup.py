#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
	name = 'django-mandrill',
	version = '0.1.0',
	#packages = ['django-mandrill',],
	packages = find_packages(),
	include_package_data = True,
	author = 'Shu Zong Chen',
	author_email = 'shu.chen@freelancedreams.com',
	description = 'Mandrill integration for Django',
	long_description = \
"""
Send emails using Mandrill as a backend.  Support for
Django's mail objects and Mandrill Templates.
""",
	license = "MIT License",
	keywords = "django mandrill email email-backend",
	classifiers = [
		'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Software Development :: Libraries :: Python Modules',
	],
	platforms = ['any'],
	url = 'https://bitbucket.org/sirpengi/django-mandrill',
	download_url = 'https://bitbucket.org/sirpengi/django-mandrill/downloads',
	install_requires = ['mandrill',],
)

