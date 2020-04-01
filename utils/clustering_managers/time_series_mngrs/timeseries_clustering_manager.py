from math import ceil
import numpy as np
from utils.data_fetcher import getTimeSeriesClusteringResultsForAlgoInFolder, getAlgoConfigStringFromFolder
import matplotlib.pyplot as plt
from config import getClusteringResultsPath, getTimeSeriesFiguresPath, getTimeSeriesToyDatasetName
from utils.clustering_managers.basic_clustering_manager import BasicClusteringManager

class TimeSeriesClusteringManager(BasicClusteringManager):
  def __init__(self):
      self.clusteringResultsPath = getClusteringResultsPath() + getTimeSeriesToyDatasetName() + '/'
      self.ownResourcesFolder = ""
      self.microClustersFolder = ""
      self.name = ""


  def main(self):
      microSnapshots = getTimeSeriesClusteringResultsForAlgoInFolder(self.microClustersFolder)
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
          self.addStyleToAx(ax=ax, DBCVscore=DBCVscore, labels=labels, t=currentTime)
          c += 1 # move to the next column
          # check if all cols were filled, and a new row must be processed
          if c == limit:
              r = r+1
              c = 0 # reset cols index
      # string representing algo config
      algoConfigString = getAlgoConfigStringFromFolder(self.ownResourcesFolder)
      self.addStyleToFig(fig, algoConfigString)
      folder = getTimeSeriesFiguresPath() + getTimeSeriesToyDatasetName() + '/' + self.name + '/'
      self.saveFig(fig, algoConfigString, folder)
      # show figure for current clustering
      plt.show()


  def createFigure(self, snapshotsAmount):
      denominator = 3
      limit = ceil(snapshotsAmount / denominator)
      rows = denominator
      cols = limit
      return limit, plt.subplots(nrows=rows, ncols=cols, sharex=True, sharey=True,)


  def addDataToAx(self, currentMicroClusters, ax, snapshotIndex):
      pass


  def getDataReqByDBCV(self, currentMicroClusters, snapshotIndex):
      pass


  def getLabels(self, currentMicroClusters, snapshotIndex):
      pass


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

  def addStyleToAx(self, ax, DBCVscore, t, labels=None):
      # add DBCV score to axes
      msg = "t: " + str(t) + ", " + "DBCV: " + str(DBCVscore)
      ax.set_aspect('equal', adjustable='box')
      ax.annotate(msg, (0, 1.17), (0, 0), xycoords='axes fraction', textcoords='offset points', va='top', ha='left',
                  fontsize=8) # FIXME: if the presence of outliers ann is no longer necessary, put (0, 1.1), (0, 0)
      if labels is not None:
          # add micro clusters and outliers presence info
          cantMicro = len(labels)
          if -1 in labels:
              cantOutliers = list(labels).count(-1)
              boolOutliers = " ⇨ " + str(cantOutliers) + " outliers"
          else:
              boolOutliers = ""
          msg = str(cantMicro) + " μc" + str(boolOutliers)
          ax.annotate(msg, (0, 1.09), (0, 0), xycoords='axes fraction', textcoords='offset points', va='top', ha='left',
                      fontsize=7)
      # gral settings
      ax.set_xbound(lower=-2, upper=2)  # TODO: |2| HARDCODED?
      ax.set_ybound(lower=-2, upper=2)
      ax.grid()












