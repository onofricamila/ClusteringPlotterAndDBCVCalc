import numpy as np

from basic_clustering_manager import BasicClusteringManager

class DenstreamClusteringManager(BasicClusteringManager):
    def __init__(self):
        super().__init__()
        self.ownResourcesFolder = self.resourcesFolder + "denstream/"
        self.microClustersFolder = self.ownResourcesFolder


    def fillFigure(self, currentMicroClusters, ax, j):
        x, y, labels = zip(*currentMicroClusters)
        ax.scatter(x, y, s=10, c=labels, cmap="nipy_spectral")


    def xAndLabels(self, currentMicroClusters, j):
        X = np.delete(currentMicroClusters, 2, 1)  # delete 3rd column of C
        x, y, labels = zip(*currentMicroClusters)
        classes = np.asarray(labels,
                             dtype=int)  # tuple to array (for the metric) IMPORTANT: also needed dtype=int instead of float
        return (X, classes)