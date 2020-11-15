import os
import sys

from pyxml2pdf.Core.Downloader import Downloader
from pyxml2pdf.Core.Initializer import Initializer


def main():
    validate_inputs()
    if not os.path.isfile(sys.argv[2]):
        Downloader(*sys.argv[1:3])
    Initializer(*sys.argv[2:])
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
