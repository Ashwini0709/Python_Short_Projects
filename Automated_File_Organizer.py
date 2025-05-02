#!/usr/bin/env Python

import os
import shutil

#Path to the folder you want to organize

folder_path = input(" Enter folder path where you want to organize your files : ")    #"/home/Ashwii/Downloads"

#Dictionary of folder names and file extensions

file_types = {
        "Images":[".jpg", ".jpeg", ".png", ".gif"],
        "Documents" : [".pdf",".docx", ".txt", ".xlsx", ".csv", ".odt"],
        "Videos": [".mp4", ".mkv", ".mov"],
        "Music": [".mp3", ".wav"],
        "Archives": [".zip", ".rar", ".tar", ".gz"],
        "Programs": [".exe", ".msi"],
        "Others": []
    }


#Create folder if not exists
for folder in file_types:
    folder_name = os.path.join(folder_path, folder)
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


#Move files to their respective folders
for filename in os.listdir(folder_path):
    file_ext = os.path.splitext(filename)[1].lower()
    file_moved = False

    for folder, extensions in file_types.items():
        if file_ext in extensions:
            src = os.path.join(folder_path, filename)
            dest = os.path.join(folder_path, folder, filename)
            shutil.move(src, dest)
            file_moved = True
            break

    #Move unknown types to "Others"
    if not file_moved and os.path.isfile(os.path.join(folder_path, filename)):
        shutil.move(os.path.join(folder_path, filename), os.path.join(folder_path, "Others", filename))



print("Files organized successfully")
    












