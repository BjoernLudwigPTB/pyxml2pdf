import os

from PyPDF2.pdf import PdfFileReader, PdfFileWriter


class PostProcessor:
    def __init__(self, path):
        """
        This creates an instance of a PostProcessor for a resulting table to
        automate splitting and rotating.

        :param str path:  path to the pdf file which shall be processed
        """
        self._path = path
        self._directory = os.path.dirname(path)
        self._name = os.path.splitext(os.path.basename(path))[0]

    def finalize_print_preparation(self):
        """
        Take the resulting multi page PDF and split into single pages while
        rotating it.

        Taken from 'https://www.blog.pythonlibrary.org/2018/04/11/splitting
        -and-merging-pdfs-with-python/' in combination with
        'https://www.johndcook.com/blog/2015/05/01/rotating-pdf-pages-with
        -python/'
        """

        pdf = PdfFileReader(self._path)
        for page_number in range(pdf.getNumPages()):
            pdf_writer = PdfFileWriter()
            page = pdf.getPage(page_number)
            page.rotateCounterClockwise(90)
            pdf_writer.addPage(page)
            output_filename = "%s_seite_%02d.pdf" % (self._name, page_number + 1)

            pdf_out = open(os.path.join(self._directory, output_filename), "wb")
            pdf_writer.write(pdf_out)
            pdf_out.close()

        print("Create ", pdf.getNumPages(), " single paged PDFs.")
