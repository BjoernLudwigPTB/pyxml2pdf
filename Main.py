import sys
from Core.Initializer import *


def validation():
    if len(sys.argv) < 4:
        raise Exception("Not enough arguments")
    if ".xml" not in sys.argv[1]:
        raise Exception("No XML file detected")
    if ".pdf" not in sys.argv[2]:
        raise Exception("File must have PDF extension")
    if ".properties" not in sys.argv[3]:
        raise Exception("Properties file must have .properties extension")


if __name__ == "__main__":
    validation()
    init = Initializer()
    init.build(sys.argv[1], sys.argv[2], sys.argv[3], Signature.AUTO_DATE)
    print("\n"
          "-------------------------------DONE-------------------------------")
