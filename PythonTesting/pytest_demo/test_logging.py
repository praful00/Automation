import logging


def test_loggingDemo():

    logger = logging.getLogger(__name__)

    filehandler = logging.FileHandler('loger.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)

    logger.setLevel(logging.CRITICAL)
    logger.debug("test executed")
    logger.info("test not executed")
    logger.warning("are you sure")
    logger.error("wrong message")
    logger.critical("critical issue")
