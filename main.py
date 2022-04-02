from utils import *
from src import logger
import template
import pathlib


app_logger=logger.get_logger(__name__,"Training.txt")


if __name__=="__main__":
    app_logger.info("Creating project folders if they do not exist")
    template.SetupTemplate()
    print(get_folder_path())
