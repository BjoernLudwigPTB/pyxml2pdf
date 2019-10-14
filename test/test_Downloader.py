from Core.Downloader import Downloader


def test_downloader_init():
    Downloader("https://github.com/")


def test_downloader_download():
    downloader = Downloader("https://www.alpinclub-berlin.de/kv/kursdaten.xml")
    downloader.download("input/kursdaten.xml")
