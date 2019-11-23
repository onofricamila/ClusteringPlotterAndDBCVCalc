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


    def fillFigure(self, currentMicroClusters, ax, j):
        labels = self.getLabels(currentMicroClusters, j)
        macro = ndarraysFormCsvsGenerator(self.macroClustersFolder)
        x, y, radius = zip(*currentMicroClusters)
        for i in range(len(x)):
            if radius[i] == 0:
                rad = 0.001
            else:
                rad = radius[i]
            if labels[j] == -1:
                color = 'black'
            else:
                color = 'green'
            circle = plt.Circle((x[i], y[i]), rad, color=color, fill=False)
            ax.add_patch(circle)
        currentMacro = macro[j]
        res2 = currentMacro['res']
        time2 = currentMacro['time']
        x2, y2, radius2 = zip(*res2)
        for k in range(len(x2)):
            circle2 = plt.Circle((x2[k], y2[k]), radius2[k], color='red', fill=False)
            ax.add_patch(circle2)


    def xAndLabels(self, currentMicroClusters, j):
        X = np.delete(currentMicroClusters, 2, 1)  # delete 3rd column of C

        # TODO: BUILD LABELS
        classes = self.getLabels(currentMicroClusters, j)
        return (X, classes)


    def getLabels(self, currentMicroClusters, currMicroIndex):
        macroClustersByTime = ndarraysFormCsvsGenerator(self.macroClustersFolder)
        labels = [-1] * len(currentMicroClusters)
        for microIndex in range(len(currentMicroClusters)):
            micro = currentMicroClusters[microIndex]
            microCircle = Circle([micro[0], micro[1]], micro[2])
            currentMacroClusters = macroClustersByTime[currMicroIndex]['res']
            for macroIndex in range(len(currentMacroClusters)):
                macro = currentMacroClusters[macroIndex]
                macroCircle = Circle([macro[0], macro[0]], macro[2])
                if self.microInsideMacro(microCircle, macroCircle):
                    labels[microIndex] = macroIndex +1 # macro index acts as label
                    break
        return np.asarray(labels)


    def microInsideMacro(self, circle1, circle2):
        distance_squared = (circle1.get_center()[0] - circle2.get_center()[0]) ** 2 + (
                    circle1.get_center()[1] - circle2.get_center()[1]) ** 2
        difference_squared = (circle2.get_radius() - circle1.get_radius()) ** 2
        return (difference_squared < distance_squared) and (circle2.get_radius() > circle1.get_radius())