import io
import os
import sys
from shutil import rmtree
import setuptools

here = os.path.abspath(os.path.dirname(__file__))

# Package meta-data.
NAME = 'sspp'
DESCRIPTION = 'Single Source Python Project'
URL = 'https://github.com/raczben/sspp'
EMAIL = 'betontalpfa@gmail.com'
AUTHOR = 'Benedek Racz'
REQUIRES_PYTHON = '>=3.4.0'
VERSION = '0.0.1'

# What packages are required for this module to be executed?
REQUIRED = []

# What packages are optional?
EXTRAS = {
    # 'fancy feature': ['django'],
}


# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION



# Where the magic happens:
setuptools.setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=['.'],

    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)