from scipy.spatial.distance import euclidean

from DBCV import validity_index
from ndarraysFormCsvsGenerator import ndarraysFormCsvsGenerator
import matplotlib.pyplot as plt

class BasicClusteringManager:
  def __init__(self):
      self.resourcesFolder = "/home/camila/Desktop/TESIS/Github_Repo_TestingMOAOnlineClustering/src/resources/denstream/"
      self.mircoClustersFolder =  self.resourcesFolder


  def main(self):
      data = ndarraysFormCsvsGenerator(self.mircoClustersFolder);
      for i in range(len(data)):
          d = data[i]
          res = d['res']
          time = d['time']
          fig = plt.gcf()
          ax = plt.gca()

          self.fillFigure(res, ax)
          index = self.calculateDBCV(res)
          self.plotFig(ax, index)


  def fillFigure(self, res, ax):
      pass


  def calculateDBCV(self, res):
      X, labels = self.xAndLabels(res)
      try:
          score = validity_index(X=X, labels=labels, metric=euclidean, per_cluster_scores=True, )
          index = round(score[0], 2)
      except ValueError as e:
          print(' Failed to calculate DBCV Index: ' + str(e))
          score = None
          index = "---"
      print(" --> score: ", score)
      return index


  def plotFig(self, ax, index):
      # add DBCV score to axes
      ax.text(x=.99, y=.93, s="DBCV: " + str(index), fontsize=10, transform=plt.gca().transAxes,
               horizontalalignment='right')
      # TODO: FOOTER WITH ALGO CONFIG?
      # fig.annotate('Something', (0, 0), (0, -20), xycoords='axes fraction', textcoords='offset points', va='top')
      # TODO: SAVE FIG IN PARAMETRIZED FOLDER
      # fig.savefig('test');
      ax.set_xbound(lower=-2, upper=2)  # TODO: |2| HARDCODED?
      ax.set_ybound(lower=-2, upper=2)
      ax.grid()
      plt.show()





