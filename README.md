# ClusteringPlotterAndDBCVCalc
Here, clustering results stored in CSV files are taken and analysed, to plot them and also calculate the DBCV score for them. 

# MOAOnlineClustering
A few MOA stream clustering algorithms are run:
* `CluStream`, and
* `DenStream`

Both taking data from a CSV file.

Their results, are also stored in CSV files.

---

## Important 
There is a `config` file, used to provide the _paths_ of the folders in which clustering results reside, and figures will be stored. Those paths, have to be specified in a **json** file. This is done because many applicatios (developed in different languages) use the same folders. Here, a `config.json` example is shown:

```json
{
    "clusteringResultsPath": "/home/camila/Desktop/TESIS/DATA/clustering_results/",
    "csvDatasetsPath": "/home/camila/Desktop/TESIS/DATA/datasets/",
    "figuresPath": "/home/camila/Desktop/TESIS/DATA/figures/",
    "timeSeriesToyDatasetName": "custom_circumferences_without_k.csv",
    "algoNames": {
	"clustream": "CluStream",
	"denstream": "DenStream"
     }
}
```
