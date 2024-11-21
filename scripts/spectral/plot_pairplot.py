import sys
from helper_functions import download_from_blob, upload_to_blob
import plotly.figure_factory as ff

storage_conn_str = sys.argv[1]
container_name = sys.argv[2]

data = download_from_blob('spectral_data_cluster', storage_conn_str, container_name)

fig = ff.create_scatterplotmatrix(data, diag='histogram', index='Cluster', height=1200, width=1200, title='Pairplot of Clusters for Spectral Clustering')

upload_to_blob(fig.to_html(), 'clusters_pairplot_spectral', storage_conn_str, container_name, folder='plots')