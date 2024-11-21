import sys
from helper_functions import download_from_blob, upload_to_blob

storage_conn_str = sys.argv[1]
container_name = sys.argv[2]

df = download_from_blob('clusters_kmeans', storage_conn_str, container_name, folder='parquets')

cluster_means = df.groupby('Cluster').mean().reset_index().round(3)
cluster_means['Count'] = df['Cluster'].value_counts().sort_index().values

upload_to_blob(cluster_means, 'cluster_means_kmeans', storage_conn_str, container_name, folder='parquets')