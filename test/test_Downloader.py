from Core.Downloader import Downloader


def test_downloader():
    Downloader("https://github.com/", "test/test_data/test_download")
