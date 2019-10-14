import pytest

from Core.Initializer import Initializer


@pytest.fixture
def download():
    from Core.Downloader import Downloader

    downloader = Downloader("https://www.alpinclub-berlin.de/kv/kursdaten.xml")
    downloader.download("input/kursdaten.xml")


def test_initializer_init():
    Initializer()


def test_initializer_build(download):
    input_folder = "input/"
    xml_filename = "kursdaten.xml"
    input_path = input_folder + xml_filename
    properties_filename = "kursdaten_prop.properties"
    properties_path = input_folder + properties_filename
    output_folder = "output/"
    output_filename = "kursdaten.pdf"
    output_path = output_folder + output_filename
    init = Initializer()
    init.build(input_path, output_path, properties_path)
