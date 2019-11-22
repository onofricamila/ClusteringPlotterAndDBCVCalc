from ndarraysFormCsvsGenerator import ndarraysFormCsvsGenerator
import matplotlib.pyplot as plt

resourcesFolder = "/home/camila/Desktop/TESIS/Github_Repo_TestingMOAOnlineClustering/src/resources/denstream/"

data = ndarraysFormCsvsGenerator(resourcesFolder);

for d in data:
    res = d['res']
    time = d['time']
    x, y, labels = zip(*res)
    plt.scatter(x, y, s=10, c=labels, cmap="nipy_spectral")
    plt.show()
