import os
import pdfkit


def intoHTML(html_path, doc, random_name):
    '''
    1. create folder with html file
    2. write html structure
    '''
    if not os.path.exists(html_path):
        os.makedirs(html_path)
    html_file = html_path + str(random_name) + '.html'

    with open(html_file, 'w') as f:
        f.write(str(doc))


def intoPDF(pdf_path, doc, random_name):
    '''
    1. create folder with pdf file
    2. convert html into pdf
    '''
    if not os.path.exists(pdf_path):
        os.makedirs(pdf_path)
    pdf_file = pdf_path + str(random_name) + '.pdf'
    pdfkit.from_string(str(doc), pdf_file)