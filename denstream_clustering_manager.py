import numpy as np

from basic_clustering_manager import BasicClusteringManager

class DenstreamClusteringManager(BasicClusteringManager):
    def __init__(self):
        super().__init__()
        self.ownResourcesFolder = self.resourcesFolder + "denstream/"
        self.microClustersFolder = self.ownResourcesFolder


    def fillFigure(self, currentMicroClusters, ax, currMicroClustersIndex):
        x, y, labels = zip(*currentMicroClusters)
        ax.scatter(x, y, s=10, c=labels, cmap="nipy_spectral")


    def getLabels(self, currentMicroClusters, currMicroClustersIndex):
        x, y, labels = zip(*currentMicroClusters)
        classes = np.asarray(labels, dtype=int)  # tuple to array (for the metric) IMPORTANT: also needed dtype=int instead of float
        return classes