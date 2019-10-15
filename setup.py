#!/usr/bin/env python

import distutils.core

try:
    import setuptools
except ImportError:
    pass

distutils.core.setup(
    name='HIMUServer',
    version="2.0",
    description="Server-side library for HyperIMU Android app",
    author='ianovir',
    author_email='info@ianovir.com',
    url='https://ianovir.com',
    packages=['.'],
    package_dir={'': '.'},
    include_package_data = True,
    classifiers=[
	  'Intended Audience :: Developers',
	  'Intended Audience :: System Administrators',
	  'Operating System :: MacOS :: MacOS X',
	  'Operating System :: Microsoft :: Windows',
	  'Operating System :: POSIX',
	  'Programming Language :: Python',
	  ],
     )
