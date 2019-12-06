from math import ceil
import numpy as np
from scipy.spatial.distance import euclidean
from utils.DBCV import validity_index
import matplotlib.pyplot as plt
from config import getClusteringResultsPath, getFiguresPath, getTimeSeriesToyDatasetName
import os

class BasicClusteringManager:
    def __init__(self):
        self.clusteringResultsPath = ""

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


    def addStyleToAx(self, ax, DBCVscore, t=None, equal=None):
        msg = ""
        # check if time stamp needs to be added (only if working w time series data clustering)
        if t is not None:
            msg = "t = " + str(t) + " | "
        # add DBCV score to axes
        msg += "DBCV: " + str(DBCVscore)
        # should be (0, 1.25), (0, 0) for non time series
        ax.annotate(msg, (0, 1.1), (0, 0), xycoords='axes fraction', textcoords='offset points', va='top', ha='left',
                    fontsize=8)
        ax.set_xbound(lower=-2, upper=2)  # TODO: |2| HARDCODED?
        ax.set_ybound(lower=-2, upper=2)
        ax.grid()
        if equal:
            ax.set_aspect('equal', adjustable='box')


    def addStyleToFig(self, fig, algoConfig):
        fig.canvas.manager.window.showMaximized()
        # format algo config str to make it more readable
        formattedAlgoConfigStr = algoConfig.replace('__', ', ')
        fig.canvas.set_window_title(self.name + ': ' + formattedAlgoConfigStr)
        fig.tight_layout()
        fig.subplots_adjust(
            top=0.951,
            bottom=0.062,
            left=0.012,
            right=0.988,
            hspace=0.249,
            wspace=0.0
        )


    def saveFig(self, fig, name, folder):
        if not os.path.exists(folder):
            os.makedirs(folder)
        fig.savefig(folder + name + '.png', dpi=300)







