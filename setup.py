from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Read, write and copy Files'
LONG_DESCRIPTION = 'A package that allows you to easily create,read and remove files and folders!'

# Setting up
setup(
    name="fstream",
    version=VERSION,
    author="DS_Stift007 (Ahmad Yosef)",
    author_email="dsstift@icloud.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    keywords=['python', 'fs', 'files', 'fstream', 'file system', 'files'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
