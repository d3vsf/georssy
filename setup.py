"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath( path.dirname( __file__ ) )

# Get the long description from the README file
with open( path.join( here, 'README.md' ), encoding = 'utf-8' ) as f:
    long_description = f.read()

setup(
    name='georssy',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.0.3',

    description='A rough Python GeoRSS decoder',
    long_description = long_description,

    # The project's main homepage.
    url='https://github.com/devsf/georssy',
    download_url = 'https://github.com/devsf/georssy/archive/0.0.3.tar.gz',

    # Author details
    author='Sergio Ferraresi',
    author_email='dev@sergioferraresi.it',

    # Choose your license
    license='Apache License 2.0',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',

        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        #'Programming Language :: Python :: 3',
        #'Programming Language :: Python :: 3.3',
        #'Programming Language :: Python :: 3.4',
        #'Programming Language :: Python :: 3.5',

        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Markup :: XML',
    ],

    keywords='georss gml decoder earthscience',

    packages=[ 'georssy' ],

    #include_package_data=True,
)
