import pandas as pd 
import glob
import os

fruitName = "Mango"
label_id = "0"

filePath = "*.txt"

folderPath = 'v4_rawData/4th_half'

dataPath = '/Users/pavankumar/Documents/Processed Datasets/' + folderPath

os.chdir( dataPath )

print(os.getcwd())

filesList = glob.glob(filePath)

print(len(filesList))



for file_ in filesList:
    print(file_)
    with open(file_) as fp:
        lines = fp.readlines()
    print(lines)
    l = ""
    if len(lines) > 0:
        for line in lines:
            newLine = line.split()
            if(len(newLine) > 0):
                newLine.pop(0)
                newLine.insert(0, label_id)
                l = l + " ".join(newLine) + '\n'

        with open(file_, "w") as fp:
            print(l,  file=fp)  
            fp.close()
    
    
    
    
    
    





'''with open("foo.txt") as fp:
    lines = fp.readlines()

print(lines)
newLines = []
l = ""
for line in lines:
    newLine = line.split()
    newLine.pop(0)
    newLine.insert(0, "Mango")
    l = l + " ".join(newLine) + '\n'
    #newLines.append(l)

with open("foo.txt", "w") as fp:
    print(l,  file=fp)  
    fp.close()'''


     

 