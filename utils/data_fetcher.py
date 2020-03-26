import json
import numpy as np
import os
from sys import exit
from config import _getTimeSeriesToyDatasetName


def getWholeDatasetClusteringResultForAlgoInFolder(resourcesFolder):
    files = getFilesIsideFolder(resourcesFolder, "csv")
    # check if there is exactly one csv file
    checkThereIsOnlyOneFile(files, section="[wholeDatasetClusteringRes]")
    # get the unique file inside folder
    fileFullName = files[0]
    filePath = resourcesFolder + fileFullName
    # return a ndarray created from the file data
    ndarray = np.genfromtxt(filePath, delimiter=",", )
    return ndarray


def getTimeSeriesClusteringResultsForAlgoInFolder(resourcesFolder):
    files = getFilesIsideFolder(resourcesFolder, "csv")
    # need to sort the files according to the timestamp
    sortedFiles = sorted(files, key=lambda x: abs(0 - int(x.split('.')[0])),) # returns a sorted list with all the files names inside the specified folder
    # for saving all the fetched data sets together
    results = []
    # iterate over the list of files
    for fileFullName in sortedFiles:
        filePath = resourcesFolder + fileFullName
        # create a ndarray with the data from the file
        ndarray = np.genfromtxt(filePath, delimiter=",", )
        time = fileFullName.split(".")[0] # time = fileNameWithoutExtention
        # append curr clustering info to the list
        results.append((
            {'time': time, 'res': ndarray}
        ))
    return results


def getSubfoldersOf(rootFolder):
    folders = filter(lambda x: os.path.isdir(os.path.join(rootFolder, x)), os.listdir(rootFolder))
    # get rid of time series data set "custom circumferences"
    filteredFolders = filter(lambda x: _getTimeSeriesToyDatasetName() not in x, folders)
    folders = list(filteredFolders)
    return folders


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
    files = getFilesIsideFolder(algoConfigFolder, "json")
    # there has to be only one config file
    checkThereIsOnlyOneFile(files, section="[algoConfig]")
    # open the file and return a dictionary simulating a json object
    fileFullName = files[0]
    filePath = algoConfigFolder + fileFullName
    with open(filePath) as algoConfigFile:
        jsonObj = json.load(algoConfigFile)
        return buildStringFromDict(jsonObj)


def getFilesIsideFolder(folder, fileType):
    fileExtention = '.' + fileType
    try:
        files = [fileName for fileName in os.listdir(folder) if fileName.endswith(fileExtention)]
    except BaseException as e:
        print("Could not open folder: " + str(e))
        exit()
    return files


def checkThereIsOnlyOneFile(files, section):
    if len(files) > 1:
        msg = "Expected one file, found many."
        print(section + " " + msg )
        exit()

