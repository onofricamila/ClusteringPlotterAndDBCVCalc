# ClusteringPlotterAndDBCVCalc
Here, clustering results stored in CSV files are analysed: they are used to generate plots, and also calculate a corresponding DBCV score.

Note that the **"algorithm configuration" file is also required**, due to the fact it is used as the figure title and name when plotting, **to see more clearly how the algo parameters influence on the resulting clustering.** A `json` file is expected at the base folder of every algorithm, having a json object with every parameter name and value.
 
### :grey_exclamation: Important: configuration 
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


**The path to the json file must be specified in the config file.**
