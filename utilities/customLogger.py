import logging
from logging import FileHandler


class LogGen:
    @staticmethod
    def log_gen():
        logger = logging.getLogger()
        fhandler: FileHandler = logging.FileHandler(filename=".\\Logs\\automation.log", mode='a')
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger
