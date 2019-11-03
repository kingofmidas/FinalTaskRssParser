class NotFound(Exception):
    pass


# print cached news
def getCache(arg_date):
    '''
    1. open and read file with news
    2. print news if their date is equal to the date in argument
    3. or raise error
    '''
    arg_date = arg_date + '\n'

    f = open('cache_news.txt', encoding='utf-8')
    lines = f.readlines()

    i = 0
    while (i < len(lines)):
        count = 0
        line = lines[i].replace('-', '')

        if(line == arg_date):
            count += 1
            print(lines[i+1], '\n', lines[i+2], '\n', lines[i+3])
        i = i + 4

    if (count == 0):
        print("Not news found on this date")
        raise NotFound

    f.close()
