from math import ceil
import numpy as np
from scipy.spatial.distance import euclidean
from utils.DBCV import validity_index
from utils.data_fetcher import getClusteringResultsInFolder, getAlgoConfigStringFromFolder
import matplotlib.pyplot as plt
from config import getClusteringResultsPath, getFiguresPath, getTimeSeriesToyDatasetName
import os
from utils.clustering_managers.basic_clustering_manager import BasicClusteringManager

class TimeSeriesClusteringManager(BasicClusteringManager):
  def __init__(self):
      self.clusteringResultsPath = getClusteringResultsPath() + getTimeSeriesToyDatasetName() + '/'
      self.ownResourcesFolder = ""
      self.microClustersFolder = ""
      self.name = ""


  def main(self):
      microSnapshots = getClusteringResultsInFolder(self.microClustersFolder)
      snapshotsAmount = len(microSnapshots)
      limit, (fig, axes) = self.createFigure(snapshotsAmount)
      # r and c are used to refer to a given subplot
      r = 0 # row index
      c = 0 # col index
      # for every row, we will fill every column
      for snapshotIndex in range(snapshotsAmount):
          snapshotInfo = microSnapshots[snapshotIndex]
          currentMicroClusters = snapshotInfo['res']
          currentTime = snapshotInfo['time']
          ax = axes[r, c]
          self.addDataToAx(currentMicroClusters, ax, snapshotIndex)
          # calculate DBCV score for the current clustering result
          X, labels = self.getDataReqByDBCV(currentMicroClusters, snapshotIndex)
          DBCVscore = self.calculateDBCV(X, labels)
          # add info and style
          self.addStyleToAx(ax=ax, DBCVscore=DBCVscore, t=currentTime, equal=True)
          c += 1 # move to the next column
          # check if all cols were filled, and a new row must be processed
          if c == limit:
              r = r+1
              c = 0 # reset cols index
      # string representing algo config
      algoConfigString = getAlgoConfigStringFromFolder(self.ownResourcesFolder)
      self.addStyleToFig(fig, algoConfigString)
      folder = getFiguresPath() + getTimeSeriesToyDatasetName() + '/' + self.name + '/'
      self.saveFig(fig, algoConfigString, folder)
      # show figure for current clustering
      plt.show()


  def createFigure(self, snapshotsAmount):
      if snapshotsAmount % 2 == 0:
          denominator = 2
      else:
          denominator = 3
      limit = ceil(snapshotsAmount / denominator)
      rows = denominator
      cols = limit
      return limit, plt.subplots(nrows=rows, ncols=cols, sharex=True, sharey=True,)


  def addDataToAx(self, currentMicroClusters, ax, snapshotIndex):
      pass


  def getDataReqByDBCV(self, currentMicroClusters, snapshotIndex):
    X = np.delete(currentMicroClusters, 2, 1)  # delete 3rd column of C
    classes = self.getLabels(currentMicroClusters, snapshotIndex)
    return (X, classes)


  # def calculateDBCV(self, X, labels):
  #     try:
  #         score = validity_index(X=X, labels=labels, metric=euclidean, per_cluster_scores=True, )
  #         customScore = round(score[0], 2)
  #     except ValueError as e:
  #         print(' Failed to calculate DBCV Index: ' + str(e))
  #         score = None
  #         customScore = "---"
  #     print(" --> score: ", score)
  #     return customScore


  def getLabels(self, currentMicroClusters, snapshotIndex):
      pass


  # def addStyleToAx(self, ax, DBCVscore, t=None, equal=None):
  #     msg = ""
  #     # check if time stamp needs to be added (only if working w time series data clustering)
  #     if t is not None:
  #         msg = "t = " + str(t) + " | "
  #     # add DBCV score to axes
  #     msg +=  "DBCV: " + str(DBCVscore)
  #     ax.annotate(msg, (0, 1.1), (0, 0), xycoords='axes fraction', textcoords='offset points', va='top', ha='left', fontsize = 8)
  #     ax.set_xbound(lower=-2, upper=2)  # TODO: |2| HARDCODED?
  #     ax.set_ybound(lower=-2, upper=2)
  #     ax.grid()
  #     if equal:
  #       ax.set_aspect('equal', adjustable='box')


  # def addStyleToFig(self, fig, algoConfig):
  #     fig.canvas.manager.window.showMaximized()
  #     # format algo config str to make it more readable
  #     formattedAlgoConfigStr = algoConfig.replace('__', ', ')
  #     fig.canvas.set_window_title(self.name + ': ' + formattedAlgoConfigStr)
  #     fig.tight_layout()
  #     fig.subplots_adjust(
  #         top=0.951,
  #         bottom=0.062,
  #         left=0.012,
  #         right=0.988,
  #         hspace=0.249,
  #         wspace=0.0
  #     )


  # def saveFig(self, fig, name):
  #     folder = getFiguresPath() + getTimeSeriesToyDatasetName() + '/' + self.name + '/'
  #     if not os.path.exists(folder):
  #         os.makedirs(folder)
  #     fig.savefig(folder + name + '.png', dpi=300)
  #












