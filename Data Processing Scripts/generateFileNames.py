import pandas as pd 
import glob
import os
folderPath = "/Users/pavankumar/Documents/Processed Datasets/TEST FOLDER/test_images"
os.chdir( folderPath )

imgList = glob.glob("*")

count = 0


writePath_v5 = "/mydrive/Yolov5_attempts/Data/test_images/"
outputFile_v5 = "images.txt"  # For YOLO v5 and tiny : they are under same google account

writePath_v4 = "/mydrive/Yolov4_attempts/Data/test_images/"
outputFile_v4  = "v4_images.txt"

localFolderPath = "/Users/pavankumar/Documents/Processed Datasets/TEST FOLDER/"

text_file = open(localFolderPath + outputFile_v4, "w")

for file_ in imgList:
    strings = writePath_v4 + file_ + "\n"
    text_file.write(strings)
text_file.close()


# This script generates the count of the all the mangoes from the labels folder.

'''for file_ in csvList:
    #print(file_)
    with open(file_) as fp:
        lines = fp.readlines()
        if len(lines):
            print(len(lines))
            count = count + len(lines)
        else:
            print("No count")
    fp.close()
print(count)'''



    
