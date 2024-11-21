import sys
from helper_functions import download_from_blob, upload_to_blob
import pandas as pd
import plotly.express as px
from sklearn.decomposition import PCA

storage_conn_str = sys.argv[1]
container_name = sys.argv[2]

data = download_from_blob('spectral_data_cluster', storage_conn_str, container_name)

pca = PCA(n_components=2)
pca_data = pca.fit_transform(data)

pca_df = pd.DataFrame(data=pca_data, columns=['PC1', 'PC2'])
pca_df['Cluster'] = data['Cluster'].values

fig = px.scatter(pca_df, x='PC1', y='PC2', color='Cluster', title='PCA of Spectral Clusters')
upload_to_blob(fig.to_html(), 'clusters_pca_spectral', storage_conn_str, container_name, folder='plots')
