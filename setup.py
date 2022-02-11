"""Install pyxml2pdf in Python path."""
import os

from setuptools import find_packages, setup  # type: ignore

current_release_version = "0.3.3"


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def readme():
    """Print long description"""
    with open("README.md") as f:
        return f.read()


setup(
    name="pyxml2pdf",
    version=current_release_version,
    description="Transfer XML to well formatted PDF table.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/BjoernLudwigPTB/pyxml2pdf",
    author=u"Björn Ludwig, Wojciech Kur",
    author_email="bjoern.ludwig@ptb.de",
    keywords="xml pdf conversion",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    documentation="pyxml2pdf.readthedocs.io",
    install_requires=["defusedxml", "download", "reportlab", "pypdf2"],
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU General Public License v3 (" "GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
