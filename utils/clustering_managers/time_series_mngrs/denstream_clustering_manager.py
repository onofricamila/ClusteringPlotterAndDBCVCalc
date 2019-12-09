import matplotlib
import numpy as np
from utils.clustering_managers.time_series_mngrs.timeseries_clustering_manager import TimeSeriesClusteringManager
from config import getDenStreamName
import matplotlib.pyplot as plt

class DenstreamClusteringManager(TimeSeriesClusteringManager):
    def __init__(self):
        super().__init__()
        self.name = getDenStreamName()
        self.ownResourcesFolder = self.clusteringResultsPath + self.name + '/'
        self.microClustersFolder = self.ownResourcesFolder


    def addDataToAx(self, currentMicroClusters, ax, snapshotIndex):
        x, y, rad, labels = zip(*currentMicroClusters)
        cmap = 'nipy_spectral'
        ax.scatter(x, y, s=10, c=labels, cmap=cmap)
        # plot micro clusters real size
        # get palette
        ns = plt.get_cmap(cmap)
        # norm palette colors
        norm = matplotlib.colors.Normalize(vmin=min(labels), vmax=max(labels))
        for microIndex in range(len(labels)):
            circle = plt.Circle((x[microIndex], y[microIndex]), rad[microIndex], color=ns(norm(labels[microIndex])),
                                     fill=False, alpha=0.3)
            ax.add_patch(circle)


    def getLabels(self, currentMicroClusters, snapshotIndex):
        x, y, rad, labels = zip(*currentMicroClusters)
        classes = np.asarray(labels, dtype=int)  # tuple to array (for the metric) IMPORTANT: also needed dtype=int instead of float
        return classes


    def getDataReqByDBCV(self, currentMicroClusters, snapshotIndex):
        X = np.delete(currentMicroClusters, 2, 1)  # delete 3rd column of C
        X2 = np.delete(X, 2, 1)  # delete 4rd column of C
        classes = self.getLabels(currentMicroClusters, snapshotIndex)
        return (X2, classes)