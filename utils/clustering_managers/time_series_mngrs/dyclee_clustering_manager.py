import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean
from utils.clustering_managers.time_series_mngrs.timeseries_clustering_manager import TimeSeriesClusteringManager
from utils.data_fetcher import getTimeSeriesClusteringResultsForAlgoInFolder
from config import getDycleeName

class DycleeClusteringManager(TimeSeriesClusteringManager):
    def __init__(self):
        super().__init__()
        self.name = getDycleeName()
        self.ownResourcesFolder = self.clusteringResultsPath + self.name + '/'
        self.microClustersFolder = self.ownResourcesFolder


    def addDataToAx(self, currentMicroClusters, ax, snapshotIndex):
        x, y, labels = zip(*currentMicroClusters)
        cmap = 'nipy_spectral'
        ax.scatter(x, y, s=10, c=labels, cmap=cmap, marker='s')


    def getLabels(self, currentMicroClusters, snapshotIndex):
        x, y, labels = zip(*currentMicroClusters)
        classes = np.asarray(labels, dtype=int)  # tuple to array (for the metric) IMPORTANT: also needed dtype=int instead of float
        return classes


    def getDataReqByDBCV(self, currentMicroClusters, snapshotIndex):
        X = np.delete(currentMicroClusters, 2, 1)  # delete 3rd column of C
        classes = self.getLabels(currentMicroClusters, snapshotIndex)
        return (X, classes)