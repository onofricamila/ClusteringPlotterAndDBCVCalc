import numpy as np
from utils.clustering_managers.basic_clustering_manager import BasicClusteringManager
from config import getDenStreamName

class DenstreamClusteringManager(BasicClusteringManager):
    def __init__(self):
        super().__init__()
        self.name = getDenStreamName()
        self.ownResourcesFolder = self.clusteringResultsPath + self.name + '/'
        self.microClustersFolder = self.ownResourcesFolder


    def addDataToAx(self, currentMicroClusters, ax, snapshotIndex):
        x, y, labels = zip(*currentMicroClusters)
        ax.scatter(x, y, s=10, c=labels, cmap="nipy_spectral")


    def getLabels(self, currentMicroClusters, snapshotIndex):
        x, y, labels = zip(*currentMicroClusters)
        classes = np.asarray(labels, dtype=int)  # tuple to array (for the metric) IMPORTANT: also needed dtype=int instead of float
        return classes