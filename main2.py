import numpy as np
from scipy.spatial.distance import euclidean

from DBCV import validity_index
from ndarraysFormCsvsGenerator import ndarraysFormCsvsGenerator
import matplotlib.pyplot as plt

resourcesFolder = "/home/camila/Desktop/TESIS/Github_Repo_TestingMOAOnlineClustering/src/resources/denstream/"

data = ndarraysFormCsvsGenerator(resourcesFolder);

for d in data:
    res = d['res']
    time = d['time']
    x, y, labels = zip(*res)
    plt.scatter(x, y, s=10, c=labels, cmap="nipy_spectral")
    # obtain scores
    X = np.delete(res, 2, 1)  # delete 3rd column of C
    classes = np.asarray(labels, dtype=int) # tuple to array (for the metric) IMPORTANT: also needed dtype=int instead of float
    try:
        score = validity_index(X=X, labels=classes, metric=euclidean, per_cluster_scores=True, )
        index = round(score[0], 2)
    except ValueError as e:
        print(' Failed to calculate DBCV Index: ' + str(e))
        score = None
        index = "---"
    print(" --> score: ", score)
    # add DBCV score to axes
    plt.text(x=.99, y=.93, s="DBCV: " + str(index), fontsize=10, transform=plt.gca().transAxes,
            horizontalalignment='right')
    # TODO: FOOTER WITH ALGO CONFIG?
    # plt.annotate('Something', (0, 0), (0, -20), xycoords='axes fraction', textcoords='offset points', va='top')
    # TODO: SAVE FIG IN PARAMETRIZED FOLDER
    # plt.savefig('test');
    plt.show()
