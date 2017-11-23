# -*- coding: utf-8 -*-

from glob import glob

DISTUTILS_DEBUG = "True"

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

config = {}

config['classifiers'] = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Scientific/Engineering',
    'Topic :: Software Development :: Code Generators',
]

setup(name='mosaicode_plugin_libmanager',
      install_requires=['Python>=2.7'],
      tests_require=[],
      test_suite='',
      version='1.0',
      packages = find_packages(exclude=["tests.*", "tests"]),
      scripts=[],
      description='Library Manager is a menu item to create and edit mosaicode libraries.',
      author='Mosaicode Group',
      author_email='',
      maintainer="Mosaicode Group",
      maintainer_email="mosaicode-dev@googlegroups.com",
      license="GNU GPL3",
      url='https://mosaicode.github.io/',

      # this is fucked up! must put it in package_data!!
      data_files=[],
      **config
      )
