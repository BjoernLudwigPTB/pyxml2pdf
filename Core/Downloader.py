import requests
from clint.textui import progress


class Downloader:
    """Download a file and store the result

    :param str url: the full download link
    :param str output_filename: the local path where and under what name to store
        the downloaded file
    """

    _url: str
    _output_filename: str

    def __init__(self, url, output_filename):
        """Download a file and store the result

        :param url: the full download link
        :param output_filename: the local path where and under what name to store
            the downloaded file
        """
        self._url = url
        self._output_filename = output_filename
        open(output_filename, "wb").write(
            requests.get(url, allow_redirects=False).content
        )

        local_filename = self.extract_filename_from_url()
        response = requests.get(url, stream=True)

        # Compute parameters for download and corresponding progress bar.
        total_length = int(response.headers.get("content-length"))
        chunk_size = 512 * 1024

        file = open(local_filename, "wb")
        for chunk in progress.bar(
            response.iter_content(chunk_size), expected_size=(total_length / 1024) + 1
        ):
            if chunk:  # filter out keep-alive new chunks
                file.write(chunk)
        file.close()

    def extract_filename_from_url(self):
        """Extract from a url the last element, i.e. the filename

        :returns str: the filename in the url
        """
        return self._url.split("/")[-1]
