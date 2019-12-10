import pytest

from pyxml2pdf import main


@pytest.mark.online
def test_all():
    from pyxml2pdf import main_predefined

    main_predefined.convert()


@pytest.mark.online
def test_init_main():
    import mock

    with mock.patch.object(main, "main", return_value=42):
        with mock.patch.object(main, "__name__", "__main__"):
            with mock.patch.object(main.sys, "exit") as mock_exit:
                main.init()

                assert mock_exit.call_args[0][0] == 42


@pytest.mark.online
def test_input():
    with pytest.raises(Exception):
        main.main()
