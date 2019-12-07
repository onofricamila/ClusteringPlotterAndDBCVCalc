import matplotlib.pyplot as plt
import numpy as np
from config import getClusteringResultsPath, getFiguresPath
from utils.data_fetcher import getSubfoldersOf, getWholeDatasetClusteringResultForAlgoInFolder
from utils.clustering_managers.basic_clustering_manager import BasicClusteringManager


class NonTimeseriesClusteringMngr(BasicClusteringManager):
  def __init__(self):
      self.clusteringResultsPath = getClusteringResultsPath()


  def main(self):
      # get the folders of the non time series datasets clustering results
      # inside them, ther is a subfolder for every algo used
      datasetsNames = getSubfoldersOf(self.clusteringResultsPath)
      firstFolder = self.clusteringResultsPath + datasetsNames[0] + '/'
      algoNames = getSubfoldersOf(firstFolder)
      print(datasetsNames)
      # get how many algorithms were used (same quantity for every dataset)
      cantAlgorithms = len(algoNames)
      cantDatasets = len(datasetsNames)
      # create figure
      fig, axes = plt.subplots(nrows=cantDatasets, ncols=cantAlgorithms, sharex=True, sharey=True)
      figFolder = getFiguresPath()
      # iterate over the data sets
      for dNameIndx in range(cantDatasets):  # row index
          dName = datasetsNames[dNameIndx]
          # iterate over the algorithms
          for algoNameIndx in range(cantAlgorithms):  # column index
              # get the current algorithm result for the data set
              algoName = algoNames[algoNameIndx]
              currFolder = self.clusteringResultsPath + dName + '/' + algoName + '/'
              X = getWholeDatasetClusteringResultForAlgoInFolder(currFolder)
              ax = axes[dNameIndx, algoNameIndx]
              # add data to axes
              x,y,labels = zip(*X)
              labels = np.asarray(labels, dtype=int)
              ax.scatter(x, y, s=10, c=labels, cmap="nipy_spectral")
              # if it's the first clustering of an algorithm, print the algo name
              if dNameIndx == 0:
                  ax.set_title(algoName, size=18)
              # obtain DBCV scores
              X = np.delete(X, 2, 1)  # delete 3rd column of C
              DBCVscore = self.calculateDBCV(X, labels)
              # add info and style
              self.addStyleToAx(ax=ax, DBCVscore=DBCVscore)
              # TODO: algos config?
      # only once ...
      fig.canvas.manager.window.showMaximized()
      fig.tight_layout(pad=0.5)
      self.saveFig(fig, "non_time_series_clustering_res", figFolder)
      # show figure for current clustering
      plt.show()


  def addStyleToAx(self, ax, DBCVscore):
      # add DBCV score to axes
      msg = "DBCV: " + str(DBCVscore)
      ax.annotate(msg, (0, 1.25), (0, 0), xycoords='axes fraction', textcoords='offset points', va='top', ha='left',
                  fontsize=8)
      # gral config
      ax.set_xbound(lower=-3, upper=3)  # TODO: |3| HARDCODED?
      ax.set_ybound(lower=-3, upper=3)
      ax.grid()
