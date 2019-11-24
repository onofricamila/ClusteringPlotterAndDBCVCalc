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


    def fillFigure(self, currentMicroClusters, ax, currMicroClustersIndex):
        labels = self.getLabels(currentMicroClusters, currMicroClustersIndex)
        macro = ndarraysFormCsvsGenerator(self.macroClustersFolder)
        x, y, radius = zip(*currentMicroClusters)
        for microIndex in range(len(x)):
            rad = self.computeRadius(radius[microIndex])
            color = self.chooseColor(labels[currMicroClustersIndex])
            # plot micro cluster
            microCircle = plt.Circle((x[microIndex], y[microIndex]), rad, color=color, fill=False)
            ax.add_patch(microCircle)
        currMacroClustersInfo = macro[currMicroClustersIndex]
        currMacroClusters = currMacroClustersInfo['res']
        x2, y2, radius2 = zip(*currMacroClusters)
        # plot all the clusters that correspond to the same time
        for macroIndex in range(len(x2)):
            macroCircle = plt.Circle((x2[macroIndex], y2[macroIndex]), radius2[macroIndex], color='red', fill=False)
            ax.add_patch(macroCircle)


    def getLabels(self, currentMicroClusters, currMicroIndex):
        macroClustersByTime = ndarraysFormCsvsGenerator(self.macroClustersFolder)
        labels = [-1] * len(currentMicroClusters)
        for microIndex in range(len(currentMicroClusters)):
            micro = currentMicroClusters[microIndex]
            microCircle = Circle(center=[micro[0], micro[1]], radius=micro[2])
            currentMacroClusters = macroClustersByTime[currMicroIndex]['res']
            for macroIndex in range(len(currentMacroClusters)):
                macro = currentMacroClusters[macroIndex]
                macroCircle = Circle([macro[0], macro[1]], macro[2])
                if macroCircle.contains(microCircle):
                    labels[microIndex] = macroIndex  # macro index acts as label
                    break
        return np.asarray(labels)


    def computeRadius(self, rad):
        if rad == 0:
            # to see a point in the plot (if rad == 0, no circle will be plotted)
            return 0.001
        else:
            return rad


    def chooseColor(self, label):
        # to denote outliers
        if label == -1:
            return 'black'
        else:
            return 'lightgreen'