import os
from os import listdir
from os.path import isfile, join

def create_folder_if_doesnt_exist(dir_name):
    # Checking if wav folder exists
    MY_DIR = dir_name
    CHECK_FOLDER = os.path.isdir(MY_DIR)

    # If folder doesn't exist, then create it.
    if not CHECK_FOLDER:
        os.makedirs(MY_DIR)
        print("created folder : ", MY_DIR)

    else:
        print(MY_DIR, "folder already exists.")


def get_files_in_folder(dir_name):
    # List all files in a folder
    file_names = [f for f in listdir(dir_name) if isfile(join(dir_name, f))]
    return file_names