import numpy as np
import os
from sys import exit
import csv

def getClusteringResultsInFolder(resourcesFolder):
    # try to get a list of all the files inside the specified folder
    try:
        files = sorted(os.listdir(resourcesFolder), key=lambda x: abs(0 - int(x.split('.')[0])),) # returns a sorted list with all the files names inside the specified folder
    except BaseException as e:
        print("Could not open resources folder: " + str(e))
        exit()
    # for saving all the fetched data sets together
    results = []
    # iterate over the list of files
    for fileFullName in files:
        filePath = resourcesFolder + fileFullName
        ndarray = np.genfromtxt(filePath, delimiter=",", ) # header must be skipped
        fileNameWithoutExtension = fileFullName.split(".")[0]
        # append info to datasets
        results.append((
            {'time': fileNameWithoutExtension, 'res': ndarray}
        ))
    return results
    
