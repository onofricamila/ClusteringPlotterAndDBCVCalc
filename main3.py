from utils.ndarraysFormCsvsGenerator import ndarraysFormCsvsGenerator
import matplotlib.pyplot as plt

resourcesFolder = "/home/camila/Desktop/TESIS/Github_Repo_TestingMOAOnlineClustering/src/resources/clustream"

macro = ndarraysFormCsvsGenerator(resourcesFolder + "/macro/");
micro = ndarraysFormCsvsGenerator(resourcesFolder + "/micro/");

for j in range(len(micro)):
    d = micro[j]
    res = d['res']
    time = d['time']
    x, y, radius = zip(*res)
    ax = plt.gca()
    ax.set_xbound(lower=-2, upper=2) # TODO: |2| HARDCODED?
    ax.set_ybound(lower=-2, upper=2)
    for i in range(len(x)):
        if radius[i] == 0:
            rad = 0.001
        else:
            rad = radius[i]
        circle = plt.Circle((x[i], y[i]), rad, color='green', fill=False)
        ax.add_patch(circle)
    currentMacro = macro[j]
    res2 = currentMacro['res']
    time2 = currentMacro['time']
    x2, y2, radius2 = zip(*res2)
    for k in range(len(x2)):
      circle2 = plt.Circle((x2[k], y2[k]), radius2[k], color='red', fill=False)
      ax.add_patch(circle2)
    plt.show()

# for d in macro:
#     res = d['res']
#     time = d['time']
#     x, y, radius = zip(*res)
#     ax = plt.gca()
#     ax.set_xbound(lower=-2, upper=2)
#     ax.set_ybound(lower=-2, upper=2)
#     for i in range(len(x)):
#         circle = plt.Circle((x[i], y[i]), radius[i], color='red', fill=False)
#         ax.add_patch(circle)
#     # obtain scores
#     # X = np.delete(res, 2, 1)  # delete 3rd column of C
#     # classes = np.asarray(radius, dtype=int) # tuple to array (for the metric) IMPORTANT: also needed dtype=int instead of float
#     # try:
#     #     score = validity_index(X=X, labels=classes, metric=euclidean, per_cluster_scores=True, )
#     #     index = round(score[0], 2)
#     # except ValueError as e:
#     #     print(' Failed to calculate DBCV Index: ' + str(e))
#     #     score = None
#     #     index = "---"
#     # print(" --> score: ", score)
#     # # add DBCV score to axes
#     # plt.text(x=.99, y=.93, s="DBCV: " + str(index), fontsize=10, transform=plt.gca().transAxes,
#     #         horizontalalignment='right')
#     # # TODO: FOOTER WITH ALGO CONFIG?
#     # # plt.annotate('Something', (0, 0), (0, -20), xycoords='axes fraction', textcoords='offset points', va='top')
#     # # TODO: SAVE FIG IN PARAMETRIZED FOLDER
#     # # plt.savefig('test');
#     plt.show()
