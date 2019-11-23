import numpy as np
import matplotlib.pyplot as plt

from basic_clustering_manager import BasicClusteringManager
from ndarraysFormCsvsGenerator import ndarraysFormCsvsGenerator


class ClustreamClusteringManager(BasicClusteringManager):
    def __init__(self):
        super().__init__()
        self.ownResourcesFolder = self.resourcesFolder + "clustream/"
        self.microClustersFolder = self.ownResourcesFolder + "micro/"
        self.macroClustersFolder = self.ownResourcesFolder + "macro/"



    def fillFigure(self, res, ax, j):
        macro = ndarraysFormCsvsGenerator(self.macroClustersFolder);
        x, y, radius = zip(*res)
        for i in range(len(x)):
            if radius[i] == 0:
                rad = 0.001
            else:
                rad = radius[i]
            circle = plt.Circle((x[i], y[i]), rad, color='green', fill=False)
            ax.add_patch(circle)
        currentMacro = macro[j]
        res2 = currentMacro['res']
        time2 = currentMacro['time']
        x2, y2, radius2 = zip(*res2)
        for k in range(len(x2)):
            circle2 = plt.Circle((x2[k], y2[k]), radius2[k], color='red', fill=False)
            ax.add_patch(circle2)

    def xAndLabels(self, res,):
        X = np.delete(res, 2, 1)  # delete 3rd column of C

        # TODO: BUILD LABELS
        classes = None # np.asarray(labels,dtype=int)  # tuple to array (for the metric) IMPORTANT: also needed dtype=int instead of float
        return (X, classes)