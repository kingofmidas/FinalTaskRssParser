import os
import logger


# print cached news
def getCache(arg_date):
    '''
    1. create file with cache news and write it
    3. or raise error
    '''
    try:
        cache_on_date = 'cache/' + str(arg_date) + '.txt'
        with open(cache_on_date, 'r', encoding='utf-8') as f:
            return f.read()

    except FileNotFoundError as e:
        logger.logging.error("FileNotFoundError: " + str(e))
        print("No such file. Please first parse news")
