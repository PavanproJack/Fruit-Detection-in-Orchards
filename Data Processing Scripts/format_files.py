import pandas as pd 
import glob
import os
folderPath = "*.csv"

csvList = glob.glob(folderPath)

for file in csvList: 

    filename, file_extension = os.path.splitext(file)
    newFileName = filename + '.txt'

    #data = pd.read_csv('justCheck.csv') 
    data = pd.read_csv(file) 

    if '#item' in data.columns:
        data.drop(['#item'], axis=1)  

    if(data.columns.get_loc("label") != 0):
        data = data[['label', 'x', 'y', 'dx', 'dy']]
        data.loc[data.label == 1, 'label'] = 'Mango'
    data['dx'] = data['x'] + data['dx']
    data['dy'] = data['y'] + data['dy']
    
    #print(data.head()) 

    export_txt = data.to_csv(newFileName, header=None, index=None, sep=' ', mode='a')

    #export_csv = data.to_csv('justCheck.csv', index = None, header=False) 
    
    