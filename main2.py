from utils.bounding_box import BoundingBox
from utils.clustering_managers.time_series_mngrs.denstream_clustering_manager import DenstreamClusteringManager
from utils.clustering_managers.time_series_mngrs.clustream_clustering_manager import ClustreamClusteringManager
from utils.clustering_managers.time_series_mngrs.dyclee_clustering_manager import DycleeClusteringManager

# time series ----------------------------------
# dataContext
dataContext = [BoundingBox(minimun=-2 , maximun=2),
               BoundingBox(minimun=-2 , maximun=2)]

# print("\n" + "DenStream")
denStreamClusMngr = DenstreamClusteringManager(dataContext)
denStreamClusMngr.main()

print("\n" + "CluStream")
cluStreamClusMngr = ClustreamClusteringManager(dataContext)
cluStreamClusMngr.main()

print("\n" + "DyClee")
dyCleeClusMngr = DycleeClusteringManager(dataContext)
dyCleeClusMngr.main()


