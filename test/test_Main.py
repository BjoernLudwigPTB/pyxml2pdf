import pytest

import Main


def test_all():
    import MainPredefined

    MainPredefined.convert()


def test_init_main():
    import mock

    with mock.patch.object(Main, "main", return_value=42):
        with mock.patch.object(Main, "__name__", "__main__"):
            with mock.patch.object(Main.sys, "exit") as mock_exit:
                Main.init()

                assert mock_exit.call_args[0][0] == 42


def test_input():
    with pytest.raises(Exception):
        Main.main()
