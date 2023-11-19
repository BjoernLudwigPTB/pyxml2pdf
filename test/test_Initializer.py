import pytest

from pyxml2pdf.core.initializer import Initializer

init_testcases = [None, "one_string", ("one_string", "two_strings")]


@pytest.mark.parametrize("teststrings", init_testcases)
def test_initializer_init(teststrings):
    with pytest.raises(TypeError):
        Initializer(teststrings)  #  type: ignore[call-arg]


def test_initializer():
    input_folder = "test/test_data/"
    xml_filename = "testdata.xml"
    input_path = input_folder + xml_filename
    output_folder = input_folder
    output_filename = "testdata.pdf"
    output_path = output_folder + output_filename
    Initializer(input_path, output_path)
