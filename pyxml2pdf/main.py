import argparse
import os
import sys

from pyxml2pdf.core.downloader import Downloader
from pyxml2pdf.core.initializer import Initializer


def _add_arguments():
    # Execute pyxml2pdf with provided command line parameters.
    parser = argparse.ArgumentParser(
        description="A converter for XML data into nicely formatted tables in a PDF."
    )
    parser.add_argument(
        "url",
        nargs="+",
        type=str,
        default="https://www.alpinclub-berlin.de/kv/DRAFT_kursdaten.xml",
        help="The URL to download XML file from if it is not present at the specified "
        "location.",
    )
    parser.add_argument(
        "path",
        nargs="+",
        type=str,
        default="input/2021_DRAFT_kursdaten.xml",
        help="The file path to store and open the XML file locally.",
    )
    parser.add_argument(
        "pdf_output",
        nargs="+",
        type=str,
        default="output/2021_DRAFT_kursdaten.pdf",
        help="The file path to store the created PDF to.",
    )
    parser.add_argument(
        "properties",
        nargs="+",
        type=str,
        default="input/kursdaten_prop.properties",
        help="The file path to the properties file, which contains the settings for "
        "the table to be created.",
    )
    return parser.parse_args()


def main():
    args = _add_arguments()
    validate_inputs()
    if not os.path.isfile(sys.argv[2]):
        Downloader(*sys.argv[1:3])
    Initializer(*sys.argv[2:4])
    print("\n-------------------------------DONE-------------------------------")


def validate_inputs():
    if len(sys.argv) < 4:
        raise ValueError(
            f"We expected four inputs in the commandline parameters, "
            f"but only {len(sys.argv)} were given. Please specify the "
            f"URL of the XML file to download. The local path to store the "
            f"downloaded file including the local filename. The output "
            f"PDF's filename and path and the properties file name and path."
        )
    if "http" not in sys.argv[1] or ".xml" not in sys.argv[1]:
        raise ValueError(
            f"Expected first commandline parameter to be the URL for downloading the "
            f"XML source file but {sys.argv[1]} was given. Please specify a valid URL "
            f"including the XML filename."
        )
    if ".xml" not in sys.argv[2]:
        raise ValueError(
            f"Expected second commandline parameter to be XML file but "
            f"{sys.argv[2]} was given. Please specify path and "
            f"name of a valid XML file."
        )
    if ".pdf" not in sys.argv[3]:
        raise ValueError(
            f"Expected third commandline parameter to be PDF path and filename "
            f"but {sys.argv[3]} was given. Please specify path and "
            f"valid filename for a PDF file."
        )
    if ".properties" not in sys.argv[4]:
        raise ValueError(
            f"Expected fourth commandline parameter to be .properties path and "
            f"filename but {sys.argv[4]} was given. Please specify path and "
            f"valid filename for a .properties file."
        )


def init():
    if __name__ == "__main__":
        sys.exit(main())


init()
