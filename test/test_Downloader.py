import pytest

from pyxml2pdf.core.downloader import Downloader


@pytest.mark.online
def test_downloader():
    Downloader(
        "https://raw.githubusercontent.com/BjoernLudwigPTB/pyxml2pdf/master/input/"
        "template.xml",
        "test/test_data/test_download",
    )
