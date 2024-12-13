import pathlib
from pathlib import Path

current_file_path_incorrect = Path('/home/den/hillel/hillel_2510/lessons/lesson_13/pathlib_base.py')
current_file_path_correct = Path(__file__)

BASE_DIR = Path(__file__).parent.parent.parent

# print(str(current_file_path_correct))
# print(current_file_path_correct.name)
# print(current_file_path_correct.parts)

print(BASE_DIR)

file_name = 'log_61224.log'
folders_from_base_dir = ['logs', 'december']

# path_to_log = pathlib.Path(BASE_DIR, 'logs', file_name)
path_to_log = pathlib.Path(BASE_DIR, *folders_from_base_dir, file_name)  # (BASE_DIR, 'logs', 'december', file_name)

with open(path_to_log) as f:
    print(f.read())


# path_not_exist = pathlib.Path(BASE_DIR, 'asd', 'sda', file_name)
#
# print(path_not_exist.parent)