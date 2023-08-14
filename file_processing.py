import os

def check_directory_existence(dir_path, target_dir):
    target_dir_lower = target_dir.lower()
    directories = os.listdir(dir_path)

    for directory in directories:
        if directory.lower() == target_dir_lower:
            return True,str(directory)
    return None,target_dir

