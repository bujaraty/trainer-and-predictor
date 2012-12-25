from distutils.core import setup
import sys
import glob

print sys.prefix
setup(
	name='CombiVEP',
	version='0.1.0',
	author='Jessada Thutkawkorapin',
	author_email='tester@test.com',
	packages=['combivep', 'combivep.engine', 'combivep.engine.test', 'combivep.refdb', 'combivep.refdb.test'],
	scripts=['bin/reference_updater'],
	url='http://pypi.python.org/pypi/combivep/',
	license='LICENSE.txt',
	description='CombiVEP',
	long_description=open('README.txt').read(),
	install_requires=[
	    "matplotlib >= 1.0.0",
	    ],
	)
