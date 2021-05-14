''' setup.py
'''

import os
import setuptools


with open(os.path.join(os.path.dirname(__file__), 'tarpy/VERSION'), 'r') as f:
    VERSION = f.read().strip()

setuptools.setup(
        name='tarpy',
        version=VERSION,
        author='m1ghtfr3e',
        description='Python Version of tar.',
        packages=setuptools.find_packages(),
	entry_points={
            'console_scripts' : [
                'tarpy = tarpy.cli.run:cli'
                ]
        },

        classifiers=[
            'Programming Language :: Python :: 3',
            'Environment :: Console',
        ],

        python_requires='>=3',
        project_urls={
            'Source' : 'https://github.com/m1ghtfr3e/tarpy'
            }
)
