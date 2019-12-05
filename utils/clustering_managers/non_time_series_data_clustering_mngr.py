from math import ceil
import matplotlib.pyplot as plt
import numpy
from scipy.spatial.distance import euclidean

from config import getClusteringResultsPath, getFiguresPath
from utils.DBCV import validity_index
from utils.data_fetcher import getSubfoldersOf, getClusteringResultsInFolder, getClusteringResultForAlgo


class NonTimeseriesDataClusteringMngr:
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
      fig, axes = plt.subplots(nrows=cantDatasets, ncols=cantAlgorithms, sharex=True, sharey=True, )
      # iterate over the data sets
      for dNameIndx in range(cantDatasets):  # row index
          dName = datasetsNames[dNameIndx]
          # iterate over the algorithms
          for algoNameIndx in range(cantAlgorithms):  # column index
              # get the current algorithm result for the data set
              algoName = algoNames[algoNameIndx]
              currFolder = self.clusteringResultsPath + dName + '/' + algoName + '/'
              X = getClusteringResultForAlgo(currFolder)
              ax = axes[dNameIndx, algoNameIndx]
              x,y,labels = zip(*X)
              labels = numpy.asarray(labels, dtype=int)
              ax.scatter(x, y, s=10, c=labels, cmap="nipy_spectral")
              # if it's the first clustering of an algorithm, print the algo name
              if dNameIndx == 0:
                  ax.set_title(algoName, size=18)
              # obtain scores
              try:
                  score = validity_index(X=X, labels=labels, metric=euclidean, per_cluster_scores=True, )
              except ValueError as e:
                  print(' Failed to calculate DBCV Index: ' + str(e))
                  score = None
              print(" --> score: ", score)
              # add DBCV score to axes
              ax.text(x=.99, y=.80, s="DBCV " + str(round(score[0], 2)), fontsize=10, transform=ax.transAxes,
                      horizontalalignment='right')
              ax.grid()
              ax.set_xbound(lower=-2, upper=2)  # TODO: |2| HARDCODED?
              ax.set_ybound(lower=-2, upper=2)
      # show subplots
      fig.canvas.manager.window.showMaximized()
      plt.show()

d = NonTimeseriesDataClusteringMngr()
d.main()
