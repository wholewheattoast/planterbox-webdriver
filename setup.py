import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

requires = [
    "planterbox",
    "selenium",
]

description = 'Steps for web testing using selenium and planterbox'

setup(name='planterbox-webdriver',
      version='0.1',
      description=description,
      classifiers=[
          "Programming Language :: Python",
      ],
      author='Nick Pilon',
      author_email='npilon@gmail.com',
      url='https://github.com/npilon/planterbox-webdriver',
      keywords='testing test bdd lettuce cucumber gherkin nosetests nose2 webdriver selenium',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=True,
      test_suite='planterbox_webdriver',
      install_requires=requires,
      )