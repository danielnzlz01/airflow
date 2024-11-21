import sys
from helper_functions import download_from_blob, upload_to_blob
from sklearn.cluster import AgglomerativeClustering
import pandas as pd

storage_conn_str = sys.argv[1]
container_name = sys.argv[2]

data_scaled = download_from_blob('scaled_df_hierarchical', storage_conn_str, container_name)
data = download_from_blob('hierarchical_data', storage_conn_str, container_name)

hierarchical = AgglomerativeClustering(n_clusters=8, metric='euclidean', linkage='ward')
data['Cluster'] = hierarchical.fit_predict(data_scaled)  # Predict clusters

data['Cluster'] = data['Cluster'].astype(str)

upload_to_blob(data, 'hierarchical_data_agglomerative', storage_conn_str, container_name)
upload_to_blob(hierarchical, 'hierarchical_agglomerative', storage_conn_str, container_name, folder='pkls')
