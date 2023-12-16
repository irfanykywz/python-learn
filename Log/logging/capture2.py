import logging, sys
#Creating a logger
logger = logging.getLogger(__name__)
logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)

#Creating a handler
def handle_unhandled_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
                #Will call default excepthook
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
        #Create a critical level log message with info from the except hook.
    logger.critical("Unhandled exception", exc_info=(exc_type, exc_value, exc_traceback))
#Assign the excepthook to the handler
sys.excepthook = handle_unhandled_exception


koqwkeqweqweqw/e/qwe/