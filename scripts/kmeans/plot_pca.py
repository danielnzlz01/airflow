import sys
from helper_functions import download_from_blob, upload_to_blob
import pandas as pd
import plotly.express as px
from sklearn.decomposition import PCA

storage_conn_str = sys.argv[1]
container_name = sys.argv[2]

df = download_from_blob('clusters_kmeans', storage_conn_str, container_name, folder='parquets')

pca = PCA(n_components=2)
pca_data = pca.fit_transform(df)
pca_df = pd.DataFrame(data=pca_data, columns=['PC1', 'PC2'])
pca_df['Cluster'] = df['Cluster'].values
fig = px.scatter(pca_df, x='PC1', y='PC2', title='PCA of Clusters', color='Cluster')

upload_to_blob(fig.to_html(), 'clusters_pca_kmeans', storage_conn_str, container_name, folder='plots')