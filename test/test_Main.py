import mock

import MainPredefined


def test_all():
    MainPredefined.convert()


def test_main():
    import Main
    with mock.patch.object(Main, "main", return_value=42):
        with mock.patch.object(Main, "__name__", "__main__"):
            with mock.patch.object(Main.sys, 'exit') as mock_exit:
                Main.init()

                assert mock_exit.call_args[0][0] == 42
