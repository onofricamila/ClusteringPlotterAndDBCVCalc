from utils.clustering_managers.time_series_mngrs.denstream_clustering_manager import DenstreamClusteringManager
from utils.clustering_managers.time_series_mngrs.clustream_clustering_manager import ClustreamClusteringManager
from utils.clustering_managers.time_series_mngrs.dyclee_clustering_manager import DycleeClusteringManager
from utils.clustering_managers.non_time_series_clustering_mngr import NonTimeseriesClusteringMngr

# by running this file, you will get

# time series ----------------------------------
# print("\n" + "DenStream")
# denStreamClusMngr = DenstreamClusteringManager()
# denStreamClusMngr.main()

# print("\n" + "CluStream")
# cluStreamClusMngr = ClustreamClusteringManager()
# cluStreamClusMngr.main()

print("\n" + "DyClee")
dyCleeClusMngr = DycleeClusteringManager()
dyCleeClusMngr.main()


# non time series ----------------------------------
# print("\n" + "Non time series clustering")
# nonTimeSeriesClusMngr = NonTimeseriesClusteringMngr()
# nonTimeSeriesClusMngr.main()