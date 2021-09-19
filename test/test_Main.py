import subprocess

import pytest
from pyxml2pdf import main


@pytest.mark.online
def test_init_main():
    main.init()


def test_validate_main():
    with pytest.raises(TypeError):
        main.validate_inputs()


def test_validate_main_with_input():
    main.validate_inputs({"local_file": "my_file.xml"})


def test_validate_main_with_invalid_input():
    with pytest.raises(ValueError):
        main.validate_inputs({"foo": "bar"})


@pytest.mark.online
def test_input():
    with pytest.raises(SystemExit):
        main.main()


def test_main_call():
    subprocess.run(
        ["python3", "-m", "pyxml2pdf.main", "input/template.xml"], check=True
    )
