import os

from PyPDF2.pdf import PageObject, PdfFileReader, PdfFileWriter


class PostProcessor:
    """Arrange for needed modifications of the result to prepare for printing

    This creates an instance of a :py:mod:`Core.PostProcessor` for a multipage PDF
    file to automate splitting and rotating.

    :param str path:  path to the PDF file which shall be processed
    """

    _path: str
    _directory: str
    _name: str

    def __init__(self, path):
        self._path = path
        self._directory = os.path.dirname(path)
        self._name = os.path.splitext(os.path.basename(path))[0]

    def finalize_print_preparation(self):
        """Take the resulting multi page PDF and split into rotated single pages

        Taken from `pythonlibrary.org
        <https://www.blog.pythonlibrary.org/2018/04/11/splitting-and-merging-pdfs
        -with-python/>`_ in combination with `johndcook.com
        <https://www.johndcook.com/blog/2015/05/01/rotating-pdf-pages-with-python/>`_
        """

        pdf: PdfFileReader = PdfFileReader(self._path)
        for page_number in range(pdf.getNumPages()):
            pdf_writer: PdfFileWriter = PdfFileWriter()
            page: PageObject = pdf.getPage(page_number)
            page.rotateCounterClockwise(90)
            pdf_writer.addPage(page)
            output_filename: str = "%s_seite_%02d.pdf" % (self._name, page_number + 1)

            pdf_out = open(os.path.join(self._directory, output_filename), "wb")
            pdf_writer.write(pdf_out)
            pdf_out.close()

        print("Create ", pdf.getNumPages(), " single paged PDFs.")
