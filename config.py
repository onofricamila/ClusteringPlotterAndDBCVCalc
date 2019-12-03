import json

clusteringResultsPath = None
figuresPath = None
algoNames = None
timeSeriesToyDatasetName = None


def fetchConfig():
    # we use the global key word to being able to change the values of the variables declared outside the function
    global clusteringResultsPath
    global figuresPath
    global algoNames
    global timeSeriesToyDatasetName

    configFilePath = "/home/camila/Desktop/TESIS/DATA/config.json"
    with open(configFilePath) as f:
        data = json.load(f)
    # fill variables
    clusteringResultsPath = data.get("clusteringResultsPath")
    figuresPath = data.get("figuresPath")
    algoNames = data.get("algoNames")
    timeSeriesToyDatasetName = data.get("timeSeriesToyDatasetName")


def getClusteringResultsPath():
    if clusteringResultsPath is not None:
        return clusteringResultsPath
    # else
    fetchConfig()
    return clusteringResultsPath


def getFiguresPath():
    if figuresPath is not None:
        return figuresPath
    # else
    fetchConfig()
    return figuresPath

def getTimeSeriesToyDatasetName():
    if timeSeriesToyDatasetName is not None:
        return timeSeriesToyDatasetName
    # else
    fetchConfig()
    return timeSeriesToyDatasetName


def getCluStreamName():
    key = "clustream"
    cluStreamName = algoNames.get(key)
    if (cluStreamName != None):
        return cluStreamName
    # else
    fetchConfig()
    return algoNames.get(key)


def getDenStreamName():
    key = "denstream"
    denStreamName = algoNames.get(key)
    if (denStreamName != None):
        return denStreamName
    # else
    fetchConfig()
    return algoNames.get(key)






