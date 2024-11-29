from functions import convert_to_24_hour

convert_to_24_hour('22:20 PM')
convert_to_24_hour('50:20 AM')
convert_to_24_hour([])
convert_to_24_hour({1:2})


# import logging
#
#
# logger_from_file = logging.getLogger('logger_from_file')
# logger_from_file.setLevel(logging.DEBUG)
#
#
# # file handler setting for errors
# file_handler = logging.FileHandler('error.log')
# file_handler.setLevel(logging.ERROR)
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# file_handler.setFormatter(formatter)
#
#
# # file handler setting for debug
# file_handler = logging.FileHandler('debug.log')
# file_handler.setLevel(logging.DEBUG)
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# file_handler.setFormatter(formatter)
#
#
# # steam handler setting
# file_handler = logging.StreamHandler()
# file_handler.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# file_handler.setFormatter(formatter)
#
#
# logger_from_file.addHandler(file_handler)
