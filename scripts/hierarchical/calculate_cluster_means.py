import sys
from helper_functions import download_from_blob, upload_to_blob

storage_conn_str = sys.argv[1]
container_name = sys.argv[2]

data = download_from_blob('hierarchical_data_agglomerative', storage_conn_str, container_name)

cluster_means = data.groupby('Cluster').mean().reset_index().round(3)
cluster_means['Count'] = data['Cluster'].value_counts().sort_index().values

upload_to_blob(cluster_means, 'cluster_means_hierarchical', storage_conn_str, container_name, folder='parquets')
upload_to_blob(data, 'hierarchical_data_agglomerative', storage_conn_str, container_name, folder='parquets')
