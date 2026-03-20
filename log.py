import logging
logging.basicConfig(
    level=logging.INFO, format='%(levelname)s - %(funcName)s :: %(lineno)d - %(message)s')
log = logging.getLogger(__name__)
DEBUG = log.debug
INFO = log.info

def setDebug():
    log.setLevel(logging.DEBUG)