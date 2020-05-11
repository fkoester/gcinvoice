# -*- coding: utf-8 -*-

from setuptools import setup
import gcinvoice


setup(
      name='gcinvoice',
      version=gcinvoice.__version__,
      author='Roman Bertle',
      author_email='bertle@smoerz.org',
      url='http://www.smoerz.org/gcinvoice',
      description='Parse Gnucash data and create invoices',
      long_description="""A module to parse Gnucash data and create invoices.

The module provides a class to parse Gnucash data files (only data relevant
for invoices is extracted), and to create invoices from templates. The module
can also be run as a script.
""",
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Financial and Insurance Industry',
          'License :: OSI Approved :: Python Software Foundation License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Topic :: Office/Business :: Financial :: Accounting',
          ],
      py_modules=['gcinvoice', 'yaptu'],
      entry_points={'console_scripts': ['gcinvoice = gcinvoice:main']},
      )
