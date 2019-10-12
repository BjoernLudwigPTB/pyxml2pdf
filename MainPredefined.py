from Core.Downloader import Downloader
from Core.Initializer import Initializer


def convert():
    input_folder = 'input/'
    domain = 'https://www.alpinclub-berlin.de/kv/'
    xml_filename = 'kursdaten.xml'
    xml_path = input_folder + xml_filename
    url = domain + xml_filename
    input_path = input_folder + xml_filename
    properties_filename = 'kursdaten_prop.properties'
    properties_path = input_folder + properties_filename
    output_folder = 'output/'
    output_filename = 'kursdaten.pdf'
    output_path = output_folder + output_filename
    dl = Downloader(url)
    dl.download(xml_path)
    init = Initializer()
    init.build(input_path, output_path, properties_path)
    print("\n"
          "-------------------------------DONE-------------------------------")


if __name__ == "__main__":
    convert()
