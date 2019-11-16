import requests


class Downloader:

    __url: str
    __output_filename: str

    def __init__(self, url, output_filename):
        """

        :param str url: the full download link
        :param str output_filename: the local path where to store the produced Pdf file
        """
        self.__url = url
        self.__output_filename = output_filename
        open(output_filename, "wb").write(
            requests.get(url, allow_redirects=False).content
        )
