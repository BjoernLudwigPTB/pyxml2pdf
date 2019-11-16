from Core.Downloader import Downloader


def test_downloader():
    Downloader(
        "https://raw.githubusercontent.com/BjoernLudwigPTB/XMLToPDFConverter/master/input/template.xml",
        "test/test_data/test_download",
    )
