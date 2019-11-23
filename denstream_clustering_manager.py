import numpy as np

from basic_clustering_manager import BasicClusteringManager

class DenstreamClusteringManager(BasicClusteringManager):
    def fillFigure(self, res, ax):
        x, y, labels = zip(*res)
        ax.scatter(x, y, s=10, c=labels, cmap="nipy_spectral")


    def xAndLabels(self, res,):
        X = np.delete(res, 2, 1)  # delete 3rd column of C
        x, y, labels = zip(*res)
        classes = np.asarray(labels,
                             dtype=int)  # tuple to array (for the metric) IMPORTANT: also needed dtype=int instead of float
        return (X, classes)