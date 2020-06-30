import pandas as pd 
import glob
import os
folderPath = "*.png"
import os

print(os.getcwd())

Images_path = "/Users/pavankumar/Documents/Robotics MSc/Dissertation/Data Pre-processing/Dissertation Datasets/mangoes/images"

fruit = "mango"

os.chdir( Images_path )
print(os.getcwd())

filesList = glob.glob(folderPath)

print(len(filesList))

sortedList = sorted(filesList)

file_name, file_ext = os.path.splitext(sortedList[0])

count = 1

print(file_ext)

for file in sortedList:
    newName = fruit + "_img_" + str(count) + file_ext

    os.rename(file, newName)

    count += 1
    
    

    

    







