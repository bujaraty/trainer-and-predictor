from setuptools import setup
#from distutils.core import setup
import sys
import glob
import pkgutil

setup(
	name='CombiVEP',
	version='0.1.0',
	author='Jessada Thutkawkorapin',
	author_email='tester@test.com',
	packages=['combivep', 'combivep.engine', 'combivep.engine.test', 'combivep.refdb', 'combivep.refdb.test', 'combivep.preproc', 'combivep.preproc.test'],
	scripts=['bin/CombiVEP_reference_updater', 'bin/CombiVEP_predictor', 'bin/CombiVEP_trainer'],
#	scripts=['bin/CombiVEP_reference_updater', 'bin/CombiVEP_predictor', 'bin/CombiVEP_trainer', 'bin/CombiVEP_demo'],
    package=['CombiVEP'],
#    package_dir={'':'combivep'},
    package_data={'': ['data/CBV/*.cbv']
                  },
    data_files=[('CombiVEP/CBV', ['combivep/data/CBV/training.cbv', 'combivep/data/CBV/test.cbv']),
                ],
	url='http://pypi.python.org/pypi/combivep/',
	license='LICENSE.txt',
	description='CombiVEP',
	long_description=open('README.txt').read(),
	install_requires=[
	    "pysam >= 0.7",
	    ],
	)


