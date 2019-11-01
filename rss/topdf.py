import pdfkit
import tohtml
import random
import os

def getPDF(url, pdf_path, limit):

    html_ = tohtml.getHTML(url, pdf_path, limit)

    rand = random.randint(1, 120)
    if not os.path.exists(pdf_path):
        os.makedirs(pdf_path)
    pdf_path = pdf_path + str(rand) + '.pdf'
    
    pdfkit.from_file(html_, pdf_path)