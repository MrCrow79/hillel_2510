import pathlib
from pathlib import Path


current_file_path_folder = Path(__file__).parent


# створити папку

new_folder = Path(current_file_path_folder, 'new_folder')
new_folder.mkdir(exist_ok=True)

new_folder3 = Path(current_file_path_folder, 'new_folder', 'new_folder2', 'new_folder3')
new_folder3.mkdir(exist_ok=True, parents=True)