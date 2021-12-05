import os
import shutil

source = input("Enter Source Folder Name: ")
destination = input("Enter Destination Folder Name: ")
source = source+'/'
destination = destination+'/'

files = os.listdir(source)
for file in files:
    shutil.copy((source+file), destination)