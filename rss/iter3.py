
class NotFound(Exception):
    pass

def getCache(argDate):
    argDate = argDate + '\n'

    f = open('cache_news.txt', encoding='utf-8')
    lines = f.readlines()

    i = 0
    while (i < len(lines)):
        count = 0
        line = lines[i].replace('-', '')

        if(line == argDate):
            count += 1
            print(lines[i+1], '\n', lines[i+2], '\n', lines[i+3])
        i = i + 4
        
    if (count == 0):
        raise NotFound

    f.close()




# f = open('parser.log')
# lines = f.readlines()
# for line in lines:
#     logDate = line.split()[1]
#     logDate = logDate.replace('-', '')
  
#     if (logDate == argDate):
#         print(line)