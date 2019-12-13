import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean
from utils.clustering_managers.time_series_mngrs.timeseries_clustering_manager import TimeSeriesClusteringManager
from utils.data_fetcher import getTimeSeriesClusteringResultsForAlgoInFolder
from config import getCluStreamName

class ClustreamClusteringManager(TimeSeriesClusteringManager):
    def __init__(self):
        super().__init__()
        self.name = getCluStreamName()
        self.ownResourcesFolder = self.clusteringResultsPath + self.name + '/'
        self.microClustersFolder = self.ownResourcesFolder + "micro/"
        self.macroClustersFolder = self.ownResourcesFolder + "macro/"


    def addDataToAx(self, currentMicroClusters, ax, snapshotIndex):
        # labels are fetched to decide micro clusters color
        labels = self.getLabels(currentMicroClusters, snapshotIndex)
        # define colors to use
        macroColor= 'red'
        microColor= 'lightgreen'
        # get all the macro clusters, which will be used to get the correct one for every micro clustering result
        macroSnapshots = getTimeSeriesClusteringResultsForAlgoInFolder(self.macroClustersFolder)
        # extract micro clusters data
        x, y, radius = zip(*currentMicroClusters)
        # move all over the micro clusters 'x' coordinate values
        for microIndex in range(len(x)):
            rad, fill = self.returnRadiusAndFillBool(radius[microIndex])
            # plot micro cluster
            microCircle = plt.Circle((x[microIndex], y[microIndex]), rad, color=microColor, fill=fill)
            ax.add_patch(microCircle)
            # get the corresponding macro clusters
        currMacroClustersInfo = macroSnapshots[snapshotIndex]
        currMacroClusters = currMacroClustersInfo['res']
        x2, y2, radius2 = zip(*currMacroClusters)
        # plot all the macro clusters that correspond to the same time
        for macroIndex in range(len(x2)):
            macroCircle = plt.Circle((x2[macroIndex], y2[macroIndex]), radius2[macroIndex], color=macroColor, fill=False, alpha=0.5)
            ax.add_patch(macroCircle)


    def getLabels(self, currentMicroClusters, snapshotIndex):
        # get all the macro clusters
        macroClustersByTime = getTimeSeriesClusteringResultsForAlgoInFolder(self.macroClustersFolder)
        labels = []
        # for every micro cluster in current snapshot
        for microIndex in range(len(currentMicroClusters)):
            micro = currentMicroClusters[microIndex]
            microCenter = [micro[0], micro[1]]
            currentMacroClusters = macroClustersByTime[snapshotIndex]['res']
            closestMacroId = -1
            minDistance = float("inf")
            # for every macro cluster in current snapshot
            for macroIndex in range(len(currentMacroClusters)):
                macro = currentMacroClusters[macroIndex]
                macroCenter = [macro[0], macro[1]]
                currDistance = euclidean(microCenter, macroCenter)
                if currDistance < minDistance:
                    minDistance = currDistance
                    closestMacroId = macroIndex
            labels.append(closestMacroId)  # macro index acts as label
        return np.asarray(labels)


    def returnRadiusAndFillBool(self, rad):
        if rad == 0:
            # to see a point in the plot (if rad == 0, no circle will be plotted)
            return (0.001, True)
        else:
            return (rad, False)


    def getDataReqByDBCV(self, currentMicroClusters, snapshotIndex):
        X = np.delete(currentMicroClusters, 2, 1)  # delete 3rd column of C
        classes = self.getLabels(currentMicroClusters, snapshotIndex)
        return (X, classes)





