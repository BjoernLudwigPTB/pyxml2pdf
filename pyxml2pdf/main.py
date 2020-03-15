import sys

from pyxml2pdf.core.initializer import Initializer


def main():
    validate()
    Initializer(sys.argv[1], sys.argv[2])
    print("\n-------------------------------DONE-------------------------------")


def validate():
    if len(sys.argv) < 2:
        raise RuntimeError("Not enough arguments")
    if ".xml" not in sys.argv[1]:
        raise RuntimeError("No XML file detected")
    if ".pdf" not in sys.argv[2]:
        raise RuntimeError("File must have PDF extension")


def init():
    if __name__ == "__main__":
        sys.exit(main())


init()
