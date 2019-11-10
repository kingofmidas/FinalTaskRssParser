import sys
from xhtml2pdf import pisa
import cgi
import html
cgi.escape = html.escape
import urllib
import urllib.parse
import urllib.request


def splithost_polyfill(url):
    parsed = urllib.parse.urlsplit(url)
    netloc = parsed[1] if parsed[1] else None
    path = parsed[2]
    path += '?' + parsed[3] if parsed[3] else ''
    path += '#' + parsed[4] if parsed[4] else ''
    return netloc, path


def convertHtmlToPdf(sourceHtml, outputFilename):
    '''
    1. replace splithost with custom function splithost_polyfill cause splithost was removed
    from python 3.8
    2. open output file for writing
    3. convert HTML to PDF
    4. close output file
    5. return True on success and False on errors
    '''
    urllib.splithost = splithost_polyfill
    urllib.request.splithost = splithost_polyfill

    resultFile = open(outputFilename, "w+b")

    pisaStatus = pisa.CreatePDF(
            sourceHtml,
            dest=resultFile)

    resultFile.close()

    return pisaStatus.err
