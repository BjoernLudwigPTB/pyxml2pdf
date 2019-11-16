import requests
from clint.textui import progress


class Downloader:

    __url: str
    __output_filename: str

    def __init__(self, url, output_filename):
        """
        Download a file and store the result.

        :param str url: the full download link
        :param str output_filename: the local path where and under what name to store
            the downloaded file
        """
        self.__url = url
        self.__output_filename = output_filename
        open(output_filename, "wb").write(
            requests.get(url, allow_redirects=False).content
        )

        local_filename = self.extract_filename_from_url()
        r = requests.get(url, stream=True)

        # Compute parameters for download and corresponding progress bar.
        total_length = int(r.headers.get("content-length"))
        chunk_size = 512 * 1024

        f = open(local_filename, "wb")
        for chunk in progress.bar(
            r.iter_content(chunk_size), expected_size=(total_length / 1024) + 1
        ):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
        f.close()

    def extract_filename_from_url(self):
        return self.__url.split("/")[-1]
