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
      for currMicroClustersIndex in range(len(microClustersByTime)):
          currMicroClustersInfo = microClustersByTime[currMicroClustersIndex]
          currentMicroClusters = currMicroClustersInfo['res']
          ax = plt.gca()
          self.fillFigure(currentMicroClusters, ax, currMicroClustersIndex)
          DBCVindex = self.calculateDBCV(currentMicroClusters, currMicroClustersIndex)
          self.plotFig(ax, DBCVindex)


  def fillFigure(self, currentMicroClusters, ax):
      pass


  def getLabels(self, currentMicroClusters, currMicroClustersIndex):
      pass


  def xAndLabels(self, currentMicroClusters, currMicroClustersIndex):
    X = np.delete(currentMicroClusters, 2, 1)  # delete 3rd column of C
    classes = self.getLabels(currentMicroClusters, currMicroClustersIndex)
    return (X, classes)


  def calculateDBCV(self, currentMicroClusters, currMicroClustersIndex):
      X, labels = self.xAndLabels(currentMicroClusters, currMicroClustersIndex)
      try:
          score = validity_index(X=X, labels=labels, metric=euclidean, per_cluster_scores=True, )
          index = round(score[0], 2)
      except ValueError as e:
          print(' Failed to calculate DBCV Index: ' + str(e))
          score = None
          index = "---"
      print(" --> score: ", score)
      return index


  def plotFig(self, ax, DBCVindex):
      # add DBCV score to axes
      ax.text(x=.99, y=.93, s="DBCV: " + str(DBCVindex), fontsize=10, transform=plt.gca().transAxes,
              horizontalalignment='right')
      # TODO: FOOTER WITH ALGO CONFIG?
      # fig.annotate('Something', (0, 0), (0, -20), xycoords='axes fraction', textcoords='offset points', va='top')
      # TODO: SAVE FIG IN PARAMETRIZED FOLDER
      # fig.savefig('test');
      ax.set_xbound(lower=-2, upper=2)  # TODO: |2| HARDCODED?
      ax.set_ybound(lower=-2, upper=2)
      ax.grid()
      f = plt.gcf()
      f.canvas.manager.window.showMaximized()
      plt.show()






