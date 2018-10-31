from Core.Initializer import *


if __name__ == "__main__":
    init = Initializer()
    init.build("input/template.xml", "output/mypdf.pdf", "input/template_prop.properties", Signature.AUTO_DATE)
    print("\n" + "--------------------------------------DONE--------------------------------------")
