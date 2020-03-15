import requests
from clint.textui import progress


class Downloader:
    """Download a file and store the result

    If no `output_filename` is specified, we extract the filename of the downloaded
    file and store the result in the *input* subfolder of the root directory.

    :param str url: the full download link
    :param str output_filename: the local path where and under what name to store
        the downloaded file
    """

    _url: str
    _output_filename: str

    def __init__(self, url, output_filename=None):
        self._url = url
        self._output_filename = output_filename

        # If no output file was given, set output filename to name of downloaded file.
        if output_filename is None:
            output_filename = self._extract_filename()

        # Get the file nd follow redirects.
        response = requests.get(url, stream=True)

        # Compute parameters for download and corresponding progress bar.
        total_length = int(response.headers.get("content-length"))
        chunk_size = 512 * 1024

        # Do the actual download by opening a file and then getting the download
        # source in chunks to avoid memory overload.
        file = open(output_filename, "wb")
        for chunk in progress.bar(
            response.iter_content(chunk_size), expected_size=(total_length / 1024) + 1
        ):
            if chunk:  # filter out keep-alive new chunks
                file.write(chunk)
        file.close()
        print("The file " + output_filename + " was successfully downloaded.")

    def _extract_filename(self):
        """Extract from a url the element after the last slash, i.e. the filename

        :returns: the filename in the url
        :rtype: str
        """
        return self._url.split("/")[-1]
