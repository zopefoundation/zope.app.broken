##############################################################################
#
# Copyright (c) 2006 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
# This package is developed by the Zope Toolkit project, documented here:
# http://docs.zope.org/zopetoolkit
# When developing and releasing this package, please follow the documented
# Zope Toolkit policies as described by this documentation.
##############################################################################
"""Setup for zope.app.broken package

"""
import os
from setuptools import setup, find_packages


def read(*rnames):
    with open(os.path.join(os.path.dirname(__file__), *rnames)) as f:
        return f.read()


setup(name='zope.app.broken',
      version='4.2',
      author='Zope Corporation and Contributors',
      author_email='zope-dev@zope.org',
      description='Zope Broken (ZODB) Object Support',
      long_description=(
          read('README.rst')
          + '\n\n' +
          read('CHANGES.rst')
      ),
      keywords="zope3 content provider",
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Framework :: Zope :: 3',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Zope Public License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Programming Language :: Python',
          'Topic :: Internet :: WWW/HTTP',
      ],
      url='http://github.com/zopefoundation/zope.app.broken',
      license='ZPL 2.1',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['zope', 'zope.app'],
      install_requires=[
          'setuptools',
          'zope.deferredimport',
          'zope.interface',
          'zope.location',
          'zope.security',
          'zope.annotation',
          'zope.processlifetime',
          'ZODB >= 3.10.0a1',
      ],
      extras_require={
          'test': [
              'mock ; python_version=="2.7"',
              'zope.browsermenu',
              'zope.browserpage',
              'zope.browserresource',
              'zope.configuration',
              'zope.testing',
              'zope.testrunner',
          ],
          'browser': [
              'zope.browsermenu',
              'zope.browserpage',
              'zope.browserresource',
          ],
      },
      include_package_data=True,
      zip_safe=False,
      )
