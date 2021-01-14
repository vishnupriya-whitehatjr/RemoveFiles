import os
import time
# replace the path with your desired path.
base_path = '/Users/vishnupriya/Desktop/GitProjects/RemoveFiles/text'

def remove_files(dir_path, n):
    all_files = os.listdir(dir_path)
    now = time.time()
    n_days = n * 86400
    for f in all_files:
        file_path = os.path.join(dir_path, f)
        if not os.path.isfile(file_path):
            continue
        if os.stat(file_path).st_mtime < now - n_days:
            os.remove(file_path)
            print("Deleted ", f)
# replace 0 with the days that you want to delete that are older! 
# Like 30 if you want to delete files that are older than 30 days!
remove_files(base_path, 0)
