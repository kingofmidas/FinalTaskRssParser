import logging

# Set basic configs for logging
fileHandler = logging.FileHandler("parser.log", "a", encoding="utf-8")
logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.DEBUG,
                    handlers=[fileHandler])
