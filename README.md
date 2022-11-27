# Binary Tree Python library

Custom Python 3 library to create and draw binary trees.

Created with [virtualenv](https://docs.python.org/3/library/venv.html).

Built with [build](https://pypa-build.readthedocs.io/en/stable/index.html).

Published with [Twine](https://pypi.org/project/twine/).

Managed with [setuptools](https://pypi.org/project/setuptools/).

### Build Process

The overall process for building a package is:

    - Create an isolated build environment.
    - Populate the build environment with build dependencies.
    - Generate the package’s metadata, if necessary and possible.
    - Generate a wheel for the package.

The wheel can then be used to perform an installation, if necessary (compressed archive, similar to Java's jar files).

### Generating Distribution packages

Run > python -m build.

The newly created /dist directory contains the tar.gz and wheel file.

The egg-info directory contains the package metadata infos, including artifacts.

### Import

To locally import the library in your Python project, download the wheel file and run > pip install /path/to/wheelfile.whl.

