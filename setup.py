from setuptools import setup, find_packages

import pathlib
import pkg_resources

with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='PyCDA',
      version='0.1.0',
      description='Python implementation CDA',
      long_description=readme(),
      classifiers=[

      ],
      keywords='',
      url='',
      author='Elia Menoni',
      author_email='eliamenoni@emenoni.eu',
      license='Proprietary',
      packages=find_packages(),
      install_requires=install_requires,
      include_package_data=True,
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'],
      entry_points={
          'console_scripts': ['PyCDA=PyCDA.run:run'],
      }
      )
