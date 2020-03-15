import subprocess

import pytest

from pyxml2pdf import Main


@pytest.mark.online
def test_all():
    from pyxml2pdf import MainPredefined

    MainPredefined.convert()


@pytest.mark.online
def test_init_main():
    import mock

    with mock.patch.object(Main, "main", return_value=42):
        with mock.patch.object(Main, "__name__", "__main__"):
            with mock.patch.object(Main.sys, "exit") as mock_exit:
                Main.init()

                assert mock_exit.call_args[0][0] == 42


@pytest.mark.online
def test_validate_main():
    with pytest.raises(RuntimeError):
        Main.validate()


@pytest.mark.online
def test_input():
    with pytest.raises(RuntimeError):
        Main.main()


def test_main_call():
    with pytest.raises(subprocess.CalledProcessError):
        subprocess.run(["python3", "-m", "pyxml2pdf.Main"], check=True)
    with pytest.raises(subprocess.CalledProcessError):
        subprocess.run(["python3", "-m", "pyxml2pdf.Main", "test.xml"], check=True)
    with pytest.raises(subprocess.CalledProcessError):
        subprocess.run(["python3", "-m", "pyxml2pdf.Main", "test.test"], check=True)
    with pytest.raises(subprocess.CalledProcessError):
        subprocess.run(
            ["python3", "-m", "pyxml2pdf.Main", "test.xml", "test.test"], check=True
        )
    with pytest.raises(subprocess.CalledProcessError):
        subprocess.run(
            ["python3", "-m", "pyxml2pdf.Main", "test.xml", "test.pdf"], check=True
        )
