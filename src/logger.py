import logging
import os
import pathlib
from utils import *

_log_format = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"


def get_file_handler(file_name):
    CreateTemplateFolders(LOGS_PATH)
    file_handler = logging.FileHandler(
        get_file_path(LOGS_PATH,file_name), mode="a"
    )
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(_log_format))
    return file_handler


def get_logger(name, file_name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(get_file_handler(file_name))
    return logger
