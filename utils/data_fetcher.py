import json

import numpy as np
import os
from sys import exit
import csv

def getClusteringResultsInFolder(resourcesFolder):
    # try to get a list of all the files inside the specified folder
    try:
        files = [fileName for fileName in os.listdir(resourcesFolder) if fileName.endswith(".csv")]
        sortedFiles = sorted(files, key=lambda x: abs(0 - int(x.split('.')[0])),) # returns a sorted list with all the files names inside the specified folder
    except BaseException as e:
        print("Could not open resources folder: " + str(e))
        exit()
    # for saving all the fetched data sets together
    results = []
    # iterate over the list of files
    for fileFullName in sortedFiles:
        filePath = resourcesFolder + fileFullName
        ndarray = np.genfromtxt(filePath, delimiter=",", ) # header must be skipped
        fileNameWithoutExtension = fileFullName.split(".")[0]
        # append info to datasets
        results.append((
            {'time': fileNameWithoutExtension, 'res': ndarray}
        ))
    return results


def buildStringFromDict(dict):
    string = ""
    i = 0 # for not adding an extra separator
    for param, value in dict.items():
        # param name and value together, separated form the others by '__'
        block = param + str(value)
        if i == 0:
            separator = ''
        else:
            separator = '__'
        string += separator + block
        i += 1
    return string

def getAlgoConfigStringFromFolder(algoConfigFolder):
    try:
        files = [fileName for fileName in os.listdir(algoConfigFolder) if fileName.endswith(".json")]
    except BaseException as e:
        print("Could not open folder: " + str(e))
        exit()

    if len(files) > 1:
        print("[algoConfig] Expected one json file, found many.")
        exit()

    fileFullName = files[0]
    filePath = algoConfigFolder + fileFullName
    with open(filePath) as algoConfigFile:
        jsonObj = json.load(algoConfigFile)
        return buildStringFromDict(jsonObj)


