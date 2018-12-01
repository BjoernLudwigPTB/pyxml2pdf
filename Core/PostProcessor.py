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

    def split(self):
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
            output_filename = '%s_seite_%02d.pdf' % (
                self._name, page_number + 1)

            pdf_out = open(os.path.join(self._directory, output_filename), 'wb')
            pdf_writer.write(pdf_out)
            pdf_out.close()

        print('Create ', pdf.getNumPages(), ' single paged PDFs.')

    @staticmethod
    def rotate(path):
        """
        Take the specified PDF and rotate it.

        Taken from 'https://www.blog.pythonlibrary.org/2018/04/11/splitting
        -and-merging-pdfs-with-python/' in combination with
        'https://www.johndcook.com/blog/2015/05/01/rotating-pdf-pages-with
        -python/'
        :param str path: the path to the pdf to rotate
        """
        _directory = os.path.dirname(path)
        _name = os.path.splitext(os.path.basename(path))[0]
        output_filename = _name + '_rotated.pdf'
        output_path = os.path.join(_directory, output_filename)

        pdf_reader = PdfFileReader(path)
        pdf_writer = PdfFileWriter()
        for page_number in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_number)
            page.rotateCounterClockwise(90)
            pdf_writer.addPage(page)

        pdf_out = open(output_path, 'wb')
        pdf_writer.write(pdf_out)
        pdf_out.close()

        print('Rotated ', output_filename, '.')

    def get_path(self):
        """
        Return the path for the PDF to postprocess.
        :return str: ppath to the pdf
        """
        return self._path
