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
    """Execute pyxml2pdf with provided command line parameters."""
    parser = argparse.ArgumentParser(
        description="A converter for XML data into nicely formatted tables in a PDF."
    )
    parser.add_argument(
        "local_file",
        nargs="+",
        type=str,
        default="input/template.xml",
        help="The local file path to the XML file. If this file is not present, "
        "the optional input parameter '--url' needs to be provided with the URL "
        "from which the file shall be downloaded.",
    )
    parser.add_argument(
        "-u",
        "--url",
        nargs=1,
        type=str,
        default=[
            "https://github.com/BjoernLudwigPTB/pyxml2pdf/blob/master/input/"
            "template.xml"
        ],
        help="The URL from which the file shall be downloaded. This is only used, "
        "if the specified local file is not present. Defaults to "
        "'https://github.com/BjoernLudwigPTB/pyxml2pdf/blob/master/input/template.xml'",
    )
    parser.add_argument(
        "-p",
        "--pdf",
        metavar="<path to Pdf file>",
        nargs=1,
        type=str,
        default=["output/template.pdf"],
        help="The file path to store the created PDF to. Defaults to "
        "'output/kursdaten.pdf'",
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
