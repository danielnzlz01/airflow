import sys
from helper_functions import download_from_blob, upload_to_blob
from sklearn.cluster import KMeans

storage_conn_str = sys.argv[1]
container_name = sys.argv[2]

data_scaled = download_from_blob('scaled_df_kmeans', storage_conn_str, container_name)
data = download_from_blob('kmeans_data', storage_conn_str, container_name)

kmeans = KMeans(n_clusters=8, random_state=42)
data['Cluster'] = kmeans.fit_predict(data_scaled)

upload_to_blob(data, 'clusters_kmeans', storage_conn_str, container_name, folder='parquets')
upload_to_blob(kmeans, 'kmeans', storage_conn_str, container_name, folder='pkls')