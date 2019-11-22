from xhtml2pdf import pisa
import urllib.request
import urllib.parse
import urllib
import html
import cgi
import sys


cgi.escape = html.escape


def splithost_polyfill(url):
    '''This function replaces deprecated splithost function.
    Same result is achieved by mean of splitting original URL into components
    and joining extracted components into host and path strings, retaining
    format of original function'''
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
    4. return True on success and False on errors
    '''
    urllib.splithost = splithost_polyfill
    urllib.request.splithost = splithost_polyfill

    with open(outputFilename, "w+b") as resultFile:
        pisaStatus = pisa.CreatePDF(
                sourceHtml,
                dest=resultFile)
        return pisaStatus.err
