from setuptools import setup
from os import path


pwd = path.abspath(path.dirname(__file__))

with open(path.join(pwd, 'docs/Readme.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='tree-inspector',
      version='2.1.0',
      python_requires='>=3.5.0',
      description='Inspect a Python object with an interactive tree view',
      url='https://github.com/slinjhu/tree-inspector',
      author='Sen Lin',
      author_email='slinjhu@gmail.com',
      license='MIT',
      packages=['tree_inspector'],
      install_requires=[
          'numpy', 'jinja2'
      ],
      zip_safe=False,
      long_description=long_description,
      long_description_content_type='text/markdown',
      include_package_data=True)

