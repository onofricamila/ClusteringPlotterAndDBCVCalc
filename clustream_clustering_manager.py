import numpy as np
import matplotlib.pyplot as plt

from basic_clustering_manager import BasicClusteringManager
from ndarraysFormCsvsGenerator import ndarraysFormCsvsGenerator
from circle import Circle

class ClustreamClusteringManager(BasicClusteringManager):
    def __init__(self):
        super().__init__()
        self.ownResourcesFolder = self.resourcesFolder + "clustream/"
        self.microClustersFolder = self.ownResourcesFolder + "micro/"
        self.macroClustersFolder = self.ownResourcesFolder + "macro/"
        self.name = "CluStream"


    def addDataToAx(self, currentMicroClusters, ax, snapshotIndex):
        # define colors to use
        microColor, outlierMicroColor, macroColor= self.defineColorsToUse()
        # labels are fetched to decide micro clusters color
        labels = self.getLabels(currentMicroClusters, snapshotIndex)
        # get all the macro clusters, which will be used to get the correct one for every micro clustering result
        macroSnapshots = ndarraysFormCsvsGenerator(self.macroClustersFolder)
        # extract micro clusters data
        x, y, radius = zip(*currentMicroClusters)
        # move all over the micro clusters 'x' coordinate values
        for microIndex in range(len(x)):
            rad, fill = self.returnRadiusAndFillBool(radius[microIndex])
            color = self.chooseColor(labels[microIndex], microColor, outlierMicroColor)
            # plot micro cluster
            microCircle = plt.Circle((x[microIndex], y[microIndex]), rad, color=color, fill=fill)
            ax.add_patch(microCircle)
            # get the corresponding macro clusters
        currMacroClustersInfo = macroSnapshots[snapshotIndex]
        currMacroClusters = currMacroClustersInfo['res']
        x2, y2, radius2 = zip(*currMacroClusters)
        # plot all the macro clusters that correspond to the same time
        for macroIndex in range(len(x2)):
            macroCircle = plt.Circle((x2[macroIndex], y2[macroIndex]), radius2[macroIndex], color=macroColor, fill=False, alpha=0.5)
            ax.add_patch(macroCircle)


    def defineColorsToUse(self):
        return 'lightgreen', 'black', 'red'


    def getLabels(self, currentMicroClusters, snapshotIndex):
        # get all the macro clusters
        macroClustersByTime = ndarraysFormCsvsGenerator(self.macroClustersFolder)
        # all micro clusters are initialized as outliers
        labels = [-1] * len(currentMicroClusters)
        # for every micro cluster in current snapshot
        for microIndex in range(len(currentMicroClusters)):
            micro = currentMicroClusters[microIndex]
            microCircle = Circle(center=[micro[0], micro[1]], radius=micro[2])
            currentMacroClusters = macroClustersByTime[snapshotIndex]['res']
            # for every macro cluster in current snapshot
            for macroIndex in range(len(currentMacroClusters)):
                macro = currentMacroClusters[macroIndex]
                macroCircle = Circle([macro[0], macro[1]], macro[2])
                # if the micro cluster is inside the current macro cluster, that means it's inside that cluster
                if macroCircle.contains(microCircle):
                    labels[microIndex] = macroIndex  # macro index acts as label
                    break # there is no need to check with other macro clusters (partitive algorithm)
        return np.asarray(labels)


    def returnRadiusAndFillBool(self, rad):
        if rad == 0:
            # to see a point in the plot (if rad == 0, no circle will be plotted)
            return (0.001, True)
        else:
            return (rad, False)


    def chooseColor(self, label, microColor, outlierMicroColor):
        # to denote outliers
        if label == -1:
            return outlierMicroColor
        else:
            return microColor


