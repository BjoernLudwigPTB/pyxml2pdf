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
        self._filename = os.path.splitext(os.path.basename(path))[0]

    def split(self):
        """
        Take the resulting multi page PDF and split into single pages.

        Taken from 'https://www.blog.pythonlibrary.org/2018/04/11/splitting
        -and-merging-pdfs-with-python/' in combination with
        'https://www.johndcook.com/blog/2015/05/01/rotating-pdf-pages-with
        -python/'
        """

        pdf = PdfFileReader(self._path)
        for page_number in range(pdf.getNumPages()):
            page = pdf.getPage(page_number)
            page.rotateCounterClockwise(90)
            pdf_writer = PdfFileWriter()
            pdf_writer.addPage(page)

            output_filename = '%s_seite_%02d.pdf' % (
                self._filename, page_number+1)

            with open(output_filename, 'wb') as out:
                pdf_writer.write(out)

        print('Create ', pdf.getNumPages(), ' single paged PDFs.')
