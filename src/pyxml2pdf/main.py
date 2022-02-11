"""Convert XML input to PDF table

This is the main point of contact to convert your XML table to Pdf. This module
is supposed to be called as a script with input parameters provided from standard in as
described in the README.
"""

import argparse
import sys
from typing import Dict

from download import download  # type: ignore
from pyxml2pdf.core.initializer import Initializer


def _add_arguments() -> Dict[str, str]:
    """Define pyxml2pdf command line parameters and help"""
    _default_download_url = (
        "https://raw.githubusercontent.com/BjoernLudwigPTB/pyxml2pdf/"
        "main/src/pyxml2pdf/input/template.xml"
    )
    parser = argparse.ArgumentParser(
        description="A converter for XML data into nicely formatted tables in a PDF."
    )
    parser.add_argument(
        "local_file",
        nargs="+",
        type=str,
        help="The local file path to the XML file. If this file is not present, "
        "it will be downloaded. The download url can be specified via the '--url' "
        "parameter.",
    )
    parser.add_argument(
        "-u",
        "--url",
        metavar="<download url>",
        nargs=1,
        type=str,
        default=[_default_download_url],
        help="The URL from which the file shall be downloaded. This is only used, "
        "if the specified 'local_file' is not present in the file system. Defaults to "
        f"'{_default_download_url}'",
    )
    parser.add_argument(
        "-p",
        "--pdf",
        metavar="<path to Pdf file>",
        nargs=1,
        type=str,
        default=["pyxml2pdf_output.pdf"],
        help="The relative file path from the current working directory and filename "
        "to store the created Pdf to. Defaults to 'pyxml2pdf_output.pdf'",
    )
    return vars(parser.parse_args())


def main():
    """This method is the workhorse of the application but expects stdin input."""
    args = _add_arguments()
    validate_inputs(args)
    download(
        args["url"][0],
        args["local_file"][0],
        replace=False,
        progressbar=True,
        verbose=False,
    )
    Initializer(args["local_file"][0], args["pdf"][0])
    print("\n-------------------------------DONE-------------------------------")


def validate_inputs(args: Dict[str, str]):
    """Checks the provided parameters on validity

    :param Dict[str, str] args: the parsed parameter namespace
    """
    if "local_file" not in args:
        raise ValueError(
            f"We expected at least the local XML as input parameter, but only {args} "
            f"were given. Please specify the local path and filename of a valid "
            f"XML file or a download URL and the path to store the file to. See "
            f"'python main.py --help' for details."
        )


def init():
    """This construct we chose to properly test command line calls of this script."""
    if __name__ == "__main__":
        sys.exit(main())


init()
