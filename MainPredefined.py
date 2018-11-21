from Core.Initializer import Initializer
from Core.Parser import Signature


def convert():
    init = Initializer()
    init.build(
        "input/kursdaten.xml", "output/kursdaten.pdf",
        "input/kursdaten_prop.properties", Signature.AUTO_DATE)
    print("\n"
          "-------------------------------DONE-------------------------------")


if __name__ == "__main__":
    convert()
