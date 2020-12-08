from utils.bounding_box import BoundingBox
from utils.clustering_managers.non_time_series_clustering_mngr import NonTimeseriesClusteringMngr

# non time series ----------------------------------
# dataContext
dataContext = [BoundingBox(minimun=-3 , maximun=3),
               BoundingBox(minimun=-3 , maximun=3)]

print("\n" + "Non time series clustering")
nonTimeSeriesClusMngr = NonTimeseriesClusteringMngr(dataContext)
nonTimeSeriesClusMngr.main()