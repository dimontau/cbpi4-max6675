from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='cbpi4-max6675',
      version='0.0.1',
      description='CraftBeerPi4 max6675 Sensor Plugin',
      author='Dmitriy Raptsevich',
      author_email='intenal@mail.ru',
      url='',
      include_package_data=True,
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.txt', '*.rst', '*.yaml'],
      'cbpi4-max6675': ['*','*.txt', '*.rst', '*.yaml']},
      packages=['cbpi4-max6675'],
      long_description=long_description,
      long_description_content_type='text/markdown'
     )
