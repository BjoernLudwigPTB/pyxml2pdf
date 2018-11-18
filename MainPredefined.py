from Core.Initializer import Initializer
from Core.Parser import Signature


if __name__ == "__main__":
    init = Initializer()
    init.build(
        "input/template.xml", "output/mypdf.pdf",
        "input/template_prop.properties", Signature.AUTO_DATE)
    print("\n"
          "-------------------------------DONE-------------------------------")
