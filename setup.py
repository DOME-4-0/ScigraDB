from setuptools import setup,  find_packages

setup(
    name='scigraDB',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/DOME-4-0/ScigraDB',
    author='Adham Hashibon',
    author_email='a.hashibon@ucl.ac.uk',
    description='Scientific Graph Data Base Utility, replacing SimPhoNy',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)

