import os
import logger


# print cached news
def getCache(arg_date):
    '''
    1. open and read file with news
    2. print news if their date is equal to the date in argument
    3. or raise error
    '''
    try:
        cache_on_date = 'cache/' + str(arg_date) + '.txt'
        with open(cache_on_date, 'r', encoding='utf-8') as f:
            return f.read()

    except FileNotFoundError as e:
        logger.logging.error("FileNotFoundError: " + str(e))
        print("No such file. Please first parse news")
