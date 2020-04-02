from scipy.spatial.distance import euclidean
from utils.DBCV import validity_index
import os

class BasicClusteringManager:
    def __init__(self, dataContext, clusteringResultsPath):
        self.clusteringResultsPath = clusteringResultsPath
        self.dataContext = dataContext


    def calculateDBCV(self, X, labels):
        try:
            score = validity_index(X=X, labels=labels, metric=euclidean, per_cluster_scores=True, )
            customScore = round(score[0], 2)
        except ValueError as e:
            print(' Failed to calculate DBCV Index: ' + str(e))
            score = None
            customScore = "---"
        print(" --> score: ", score)
        return customScore


    def saveFig(self, fig, name, folder):
        if not os.path.exists(folder):
            os.makedirs(folder)
        fig.savefig(folder + name + '.png', dpi=300)


    def setAxBoundaries(self, ax):
        xbound = self.dataContext[0]
        ybound = self.dataContext[1]
        ax.set_xbound(lower=xbound.minimun, upper=xbound.maximun)
        ax.set_ybound(lower=ybound.minimun, upper=ybound.maximun)






