import os
import shutil
from collections import Counter
from datetime import datetime

def get_common_year(file_list):
    years = [datetime.fromtimestamp(os.path.getctime(file)).year for file in file_list]
    common_year = Counter(years).most_common(1)[0][0]
    return common_year

def move_parent_folder(source_folder, common_year):
    destination_folder = os.path.join(os.path.dirname(source_folder), str(common_year))
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    shutil.move(source_folder, destination_folder)

def get_all_files_in_subfolder(subfolder, depth=1):
    files = []
    for entry in os.scandir(subfolder):
        if entry.is_file():
            files.append(entry.path)
        elif entry.is_dir() and depth > 0:
            files.extend(get_all_files_in_subfolder(entry.path, depth - 1))
    return files

def main():
    parent_folder = input("Enter the path to the parent folder: ")
    subfolders = [os.path.join(parent_folder, d) for d in os.listdir(parent_folder) if os.path.isdir(os.path.join(parent_folder, d))]
    
    for subfolder in subfolders:
        files = get_all_files_in_subfolder(subfolder, depth=1)
        if files:
            common_year = get_common_year(files)
            move_parent_folder(subfolder, common_year)
            print(f"Moved '{subfolder}' to '{common_year}' folder.")

if __name__ == "__main__":
    main()