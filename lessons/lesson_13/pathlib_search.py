from pathlib import Path
import os

base_path = Path(__file__).parent.parent.parent

all_ = [k for k in base_path.iterdir()]

all_folders = [k for k in base_path.iterdir() if k.is_dir()]
all_files = [k for k in base_path.iterdir() if k.is_file()]
all_log_files = [k for k in base_path.iterdir() if k.is_file() and k.name.endswith('.log')]

# print(*all_log_files, sep='\n')
path_not_exist = Path(base_path, 'asd', 'sda', 'asd.loc')

# print(path_not_exist.exists(), path_not_exist)
# print(all_log_files[0].exists(), all_log_files[0])
# print(*all_log_files, sep='\n')

# example_file_name = ['collect_gw0.log', 'collect_gw1.log', 'collect_gw2.log', 'collect_gw3.log', 'collect_gw4.log']


log_files_folder = Path(base_path, 'logs')

file_name_example = 'collect_gw{}.log'

counter = 0
file_collector = []
while True:
    # path_ = Path(log_files_folder, file_name_example.format(counter))
    path_ = Path(log_files_folder, f'collect_gw{counter}.log')
    if path_.exists():
        file_collector.append(str(path_))
    else:
        break
    counter += 1

# print(file_collector)


# всі файли з base_path які закінчуться на .log

all_logs = []
# for dir_path, folders, files in os.walk(str(base_path)):
for all_objs in os.walk(str(base_path)):  # all_objs - tuple. dir_path, folders, files = all_objs
    dir_path = all_objs[0]
    folders = all_objs[1]
    files = all_objs[2]

    # dir_path, folders, files = all_objs
    for file_name in files:
        if file_name.endswith('.log'):
            all_logs.append(str(Path(dir_path, file_name)))

print(*all_logs, sep='\n')