import sys

from pyxml2pdf.Core.Initializer import Initializer


def main():
    validate()
    Initializer(*sys.argv[1:])
    print("\n-------------------------------DONE-------------------------------")


def validate():
    if len(sys.argv) < 3:
        raise ValueError(
            f"We expected three inputs in the commandline parameters, "
            f"but only {len(sys.argv)} were given. Please specify the "
            f"URL of the XML file to download or read in, the output "
            f"PDF's filename and path and the properties file name."
        )
    if ".xml" not in sys.argv[1]:
        raise ValueError(
            f"Expected first commandline parameter to be XML file but "
            f"{sys.argv[1]} was given. Please specify path and "
            f"name of a valid XML file."
        )
    if ".pdf" not in sys.argv[2]:
        raise ValueError(
            f"Expected second commandline parameter to be PDF path and filename "
            f"but {sys.argv[2]} was given. Please specify path and "
            f"valid filename for a PDF file."
        )
    if ".properties" not in sys.argv[3]:
        raise ValueError(
            f"Expected third commandline parameter to be .properties path and filename "
            f"but {sys.argv[3]} was given. Please specify path and "
            f"valid filename for a .properties file."
        )


def init():
    if __name__ == "__main__":
        sys.exit(main())


init()
