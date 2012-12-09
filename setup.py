from distutils.core import setup

setup(
	name='MyTowel',
	version='0.1.0',
	author='test A. bc',
	author_email='tester@test.com',
	packages=['mytowel', 'mytowel.test'],
	scripts=['bin/test_bin.py'],
	url='http://pypi.python.org/pypi/TowelStuff/',
	license='LICENSE.txt',
	description='Useful MyTowel stuff.',
	long_description=open('README.txt').read(),
	install_requires=[
	    "matplotlib >= 1.0.0",
	    ],
	)
