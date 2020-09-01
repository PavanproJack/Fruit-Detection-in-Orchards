import pandas as pd 
import glob
import os
folderPath = "/Users/pavankumar/Documents/Processed Datasets/TEST FOLDER/labels"
os.chdir( folderPath )

csvList = glob.glob("*.txt")
#print(csvList)

count = 0
print(len(csvList))

for file_ in csvList:
    #print(file_)
    with open(file_) as fp:
        lines = fp.readlines()
        if len(lines):
            print(len(lines))
            count = count + len(lines)
        else:
            print("No count")
    fp.close()
print(count)

    
