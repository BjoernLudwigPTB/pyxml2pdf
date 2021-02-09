from pyxml2pdf.core.downloader import Downloader
from pyxml2pdf.core.initializer import Initializer


def convert():
    input_folder = "input/"
    domain = "https://www.alpinclub-berlin.de/kv/"
    xml_filename = "DRAFT_kursdaten.xml"
    xml_path = input_folder + xml_filename
    url = domain + xml_filename
    input_path = input_folder + xml_filename
    output_folder = "output/"
    output_filename = "2021_DRAFT_kursdaten.pdf"
    output_path = output_folder + output_filename
    Downloader(url, xml_path)
    Initializer(input_path, output_path)
    print("\n-------------------------------DONE-------------------------------")


if __name__ == "__main__":
    convert()
