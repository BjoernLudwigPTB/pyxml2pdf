from Core.Initializer import Initializer
from Core.Parser import Signature


def convert():
    init = Initializer()
    init.build(
        "input/template.xml", "output/mypdf.pdf",
        "input/template_prop.properties", Signature.AUTO_DATE)
    print("\n"
          "-------------------------------DONE-------------------------------")


if __name__ == "__main__":
    convert()
