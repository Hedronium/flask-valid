
from distutils.core import setup

setup(
		name="flask-valid",
		version="0.10",
		py_modules = ['lib.app'],
		packages = ['flask-valid'],
		description='Laravel like form validator for flask',
		install_requires=[

		],
		url='https://github.com/Hedronium/pyloop',
		#download_url = 'https://github.com/Hedronium/pyloop/tarball/0.18',
		author = 'Hedronium',
		keywords = ['form validator','python 3','flask','form validator for flask'],
		author_email= 'project.anik@gmail.com',
		licence='MIT'
)