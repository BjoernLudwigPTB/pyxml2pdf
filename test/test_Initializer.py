import pytest

from pyxml2pdf.Core.Initializer import Initializer

init_testcases = [None, "one_string", ("one_string", "two_strings")]


@pytest.mark.parametrize("teststrings", init_testcases)
def test_initializer_init(teststrings):
    with pytest.raises(TypeError):
        Initializer(teststrings)


def test_initializer():
    input_folder = "test/test_data/"
    xml_filename = "testdata.xml"
    input_path = input_folder + xml_filename
    properties_filename = "testdata_prop.properties"
    properties_path = input_folder + properties_filename
    output_folder = input_folder
    output_filename = "testdata.pdf"
    output_path = output_folder + output_filename
    Initializer(input_path, output_path, properties_path)
