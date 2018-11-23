import pytest

from Core.Initializer import Initializer


@pytest.fixture
def download():
    from Core.Downloader import Downloader
    dl = Downloader('https://alpinclub-berlin.de/kv/kursdaten.xml')
    dl.download('input/kursdaten.xml')


def test_initializer_init():
    Initializer()


def test_initializer_build(download):
    pass
