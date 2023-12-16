import logging, sys, traceback
logger = logging.getLogger('logger')
fh = logging.FileHandler('test.log')
logger.addHandler(fh)
def exc_handler(exctype, value, tb):
    logger.exception(''.join(traceback.format_exception(exctype, value, tb)))
sys.excepthook = exc_handler
print("hello")
1/0