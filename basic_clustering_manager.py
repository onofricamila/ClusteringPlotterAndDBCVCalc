from math import floor, ceil

import numpy as np
from scipy.spatial.distance import euclidean

from DBCV import validity_index
from ndarraysFormCsvsGenerator import ndarraysFormCsvsGenerator
import matplotlib.pyplot as plt

class BasicClusteringManager:
  def __init__(self):
      self.resourcesFolder = "/home/camila/Desktop/TESIS/Github_Repo_TestingMOAOnlineClustering/src/resources/"
      self.ownResourcesFolder = ""
      self.microClustersFolder = ""


  def main(self):
      microClustersByTime = ndarraysFormCsvsGenerator(self.microClustersFolder)
      # configure fig
      snapshotsAmount = len(microClustersByTime)
      if snapshotsAmount % 2 == 0:
          denominator = 2
      else:
          denominator = 3
      limit = ceil(snapshotsAmount/denominator)
      rows = denominator
      cols = limit
      fig, axes = plt.subplots(nrows=rows, ncols=cols, sharex=True, sharey=True,)
      r = 0
      c = 0
      for currTimeIndex in range(snapshotsAmount):
          currMicroClustersInfo = microClustersByTime[currTimeIndex]
          currentMicroClusters = currMicroClustersInfo['res']
          currentTime = currMicroClustersInfo['time']
          ax = axes[r, c]
          self.fillFigure(currentMicroClusters, ax, currTimeIndex)
          DBCVindex = self.calculateDBCV(currentMicroClusters, currTimeIndex)

          self.plotFig(ax, DBCVindex, currentTime)
          c += 1
          # org axes
          if c == limit:
              r = r+1
              c = 0

      # show
      fig = plt.gcf()
      fig.canvas.manager.window.showMaximized()
      fig.canvas.set_window_title('Test')
      plt.tight_layout()
      plt.subplots_adjust(
          top=0.951,
          bottom=0.062,
          left=0.012,
          right=0.988,
          hspace=0.249,
          wspace=0.0
      )
      plt.show()


  def fillFigure(self, currentMicroClusters, ax, currTimeIndex):
      pass


  def getLabels(self, currentMicroClusters, currTimeIndex):
      pass


  def xAndLabels(self, currentMicroClusters, currTimeIndex):
    X = np.delete(currentMicroClusters, 2, 1)  # delete 3rd column of C
    classes = self.getLabels(currentMicroClusters, currTimeIndex)
    return (X, classes)


  def calculateDBCV(self, currentMicroClusters, currTimeIndex):
      X, labels = self.xAndLabels(currentMicroClusters, currTimeIndex)
      try:
          score = validity_index(X=X, labels=labels, metric=euclidean, per_cluster_scores=True, )
          index = round(score[0], 2)
      except ValueError as e:
          print(' Failed to calculate DBCV Index: ' + str(e))
          score = None
          index = "---"
      print(" --> score: ", score)
      return index


  def plotFig(self, ax, DBCVindex, t):
      # add DBCV score to axes
      ax.annotate("t = "+ str(t)+ " | DBCV: " + str(DBCVindex), (0, 1.1), (0, 0), xycoords='axes fraction', textcoords='offset points', va='top', ha='left')
      # TODO: FOOTER WITH ALGO CONFIG?
      # TODO: SAVE FIG IN PARAMETRIZED FOLDER
      # fig.savefig('test');
      ax.set_xbound(lower=-2, upper=2)  # TODO: |2| HARDCODED?
      ax.set_ybound(lower=-2, upper=2)
      ax.grid()
      ax.set_aspect('equal', adjustable='box')







