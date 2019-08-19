from setuptools import setup, find_packages
import os

version = '0.7.1.dev0'

setup(name='uvc.validation',
      version=version,
      description="uvc validation addon",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Dominik Jaskolka',
      author_email='admin@bequick.at',
      url='http://uvwebcommunity.bg-kooperation.de/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['uvc'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'z3c.testsetup',
          'zope.schema',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = uvcsite 
      """,
      )
