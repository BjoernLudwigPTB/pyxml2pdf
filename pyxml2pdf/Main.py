import sys

from pyxml2pdf.Core.Initializer import Initializer


def main():
    validate()
    Initializer(sys.argv[1], sys.argv[2])
    print("\n-------------------------------DONE-------------------------------")


def validate():
    if len(sys.argv) < 2:
        raise Exception("Not enough arguments")
    if ".xml" not in sys.argv[1]:
        raise Exception("No XML file detected")
    if ".pdf" not in sys.argv[2]:
        raise Exception("File must have PDF extension")


def init():
    if __name__ == "__main__":
        sys.exit(main())


init()
