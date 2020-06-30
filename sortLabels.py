import pandas as pd 
import glob
import os
folderPath = "*.csv"
import os

print(os.getcwd())

Labels_path = "/Users/pavankumar/Documents/Robotics MSc/Dissertation/Data Pre-processing/Dissertation Datasets/mangoes/Labels"
#Images_path = "/Users/pavankumar/Documents/Robotics MSc/Dissertation/Data Pre-processing/Dissertation Datasets/mangoes/images"

fruit = "mango"

os.chdir( Labels_path )
print(os.getcwd())

filesList = glob.glob(folderPath)

print(len(filesList))

sortedList = sorted(filesList)

file_name, file_ext = os.path.splitext(sortedList[0])

count = 1

#print(sortedList)

for file in sortedList:
    newName = fruit + "_img_" + str(count) + ".txt"
    
    data = pd.read_csv(file) 
    
    if '#item' in data.columns:
        data.drop(['#item'], axis=1)  

    if(data.columns.get_loc("label") != 0):
        data = data[['label', 'x', 'y', 'dx', 'dy']]
        data.loc[data.label == 1, 'label'] = fruit
    data['dx'] = data['x'] + data['dx']
    data['dy'] = data['y'] + data['dy']

    export_txt = data.to_csv(newName, header=False, index=False, sep=' ', mode='a')

    #os.rename(file, newName)

    count += 1

    '''if(count == 3):
        break'''
    

    

    







