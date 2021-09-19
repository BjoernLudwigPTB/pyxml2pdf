"""This module contains the class :class:`PostProcessor` to arrange the result pages"""

import os

from PyPDF2.pdf import PageObject, PdfFileReader, PdfFileWriter  # type: ignore


class PostProcessor:
    """Arrange for needed modifications of the result to prepare for printing

    This creates an instance of a :py:mod:`pyxml2pdf.core.post_processor` for a
    multipage PDF file to automate splitting and rotating.

    :param str path:  path to the PDF file which shall be processed
    """

    _full_output_path_: str
    _output_directory_name: str
    _output_base_filename: str

    def __init__(self, path):
        self._full_output_path_ = path
        self._output_directory_name = os.path.dirname(path)
        self._output_base_filename = os.path.splitext(os.path.basename(path))[0]

    def finalize_print_preparation(self):
        """Take the resulting multi page PDF and split into rotated single pages

        Taken from `pythonlibrary.org
        <https://www.blog.pythonlibrary.org/2018/04/11/splitting-and-merging-pdfs
        -with-python/>`_ in combination with `johndcook.com
        <https://www.johndcook.com/blog/2015/05/01/rotating-pdf-pages-with-python/>`_
        """

        pdf: PdfFileReader = PdfFileReader(self._full_output_path_)
        for page_number in range(pdf.getNumPages()):
            pdf_writer: PdfFileWriter = PdfFileWriter()
            page: PageObject = pdf.getPage(page_number)
            page.rotateCounterClockwise(90)
            pdf_writer.addPage(page)
            output_filename: str = (
                f"{self._output_base_filename}_page_"
                f"{str(page_number + 1).zfill(2)}.pdf"
            )

            with open(
                os.path.join(self._output_directory_name, output_filename), "wb"
            ) as pdf_out:
                pdf_writer.write(pdf_out)

        path_to_pdf = os.path.join(os.getcwd(), self._full_output_path_)
        print(
            f"Create {pdf.getNumPages()} single paged PDFs.\n\n"
            f"You can find them concatenated at file://"
            f"{path_to_pdf}"
        )
