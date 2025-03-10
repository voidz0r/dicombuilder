from distutils.core import setup

setup(
    # Application name:
    name="dicombuilder",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="void",
    author_email="void@voidzone.it",

    # Packages
    packages=["dicombuilder"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="http://pypi.python.org/pypi/dicombuilder/",

    #
    # license="LICENSE.txt",
    description="DICOM Builder © 2024 by void is licensed under CC BY 4.0. \
            To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
        "",
    ],
)
