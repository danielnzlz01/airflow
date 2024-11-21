import sys
from helper_functions import download_from_blob, upload_to_blob
from sklearn.cluster import SpectralClustering
import pandas as pd

storage_conn_str = sys.argv[1]
container_name = sys.argv[2]

data_scaled = download_from_blob('scaled_df_spectral', storage_conn_str, container_name)
data = download_from_blob('spectral_data', storage_conn_str, container_name)

spectral = SpectralClustering(n_clusters=8, affinity='nearest_neighbors', random_state=42)
data['Cluster'] = spectral.fit_predict(data_scaled).astype(str)

upload_to_blob(data, 'spectral_data_cluster', storage_conn_str, container_name)
upload_to_blob(spectral, 'spectral_cluster', storage_conn_str, container_name, folder='pkls')
