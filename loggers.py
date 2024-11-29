import logging.config
import os

from utils import BASE_DIR

logging.config.fileConfig(os.path.join(BASE_DIR, 'logging_config.ini'))


sample_logger = logging.getLogger('sampleLogger')



logger_from_file = logging.getLogger('logger_from_file')
logger_from_file.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# file handler setting for errors
error_file_handler = logging.FileHandler('error.log')

error_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s ||| func_name is %(funcName)s')
error_file_handler.setLevel(logging.ERROR)
error_file_handler.setFormatter(error_formatter)


# file handler setting for debug
debug_file_handler = logging.FileHandler('debug.log')
debug_file_handler.setLevel(logging.DEBUG)
debug_file_handler.setFormatter(formatter)


# steam handler setting
steam_handler = logging.StreamHandler()
steam_handler.setLevel(logging.INFO)
steam_handler.setFormatter(formatter)


logger_from_file.addHandler(error_file_handler)
logger_from_file.addHandler(debug_file_handler)
logger_from_file.addHandler(steam_handler)