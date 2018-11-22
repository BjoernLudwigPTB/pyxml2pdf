from Core.Downloader import Downloader


def test_downloader_init():
    Downloader('https://github.com/')


def test_downloader_download():
    dl = Downloader('https://alpinclub-berlin.de/kv/kursdaten.xml')
    dl.download('input/kursdaten.xml')
