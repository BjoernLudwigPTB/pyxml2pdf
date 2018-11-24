import pytest

import Main


def test_all():
    import MainPredefined
    MainPredefined.convert()


def test_init_main():
    import Main
    import mock
    with mock.patch.object(Main, "main", return_value=42):
        with mock.patch.object(Main, "__name__", "__main__"):
            with mock.patch.object(Main.sys, 'exit') as mock_exit:
                Main.init()

                if mock_exit.call_args[0][0] != 42:
                    raise AssertionError()


class TestMain:

    def test_input(self):
        with pytest.raises(Exception):
            Main.main()
