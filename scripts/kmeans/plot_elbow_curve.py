import sys
from helper_functions import download_from_blob, upload_to_blob
from sklearn.cluster import KMeans
import plotly.graph_objects as go

storage_conn_str = sys.argv[1]
container_name = sys.argv[2]

data_scaled = download_from_blob('scaled_df_kmeans', storage_conn_str, container_name)
inertia = []
k_range = range(2, 17)
for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(data_scaled)
    inertia.append(kmeans.inertia_)

fig = go.Figure(data=go.Scatter(x=list(k_range), y=inertia, mode='lines+markers'))
fig.update_layout(title='Elbow Method For Optimal k', xaxis_title='Number of clusters', yaxis_title='Inertia')
upload_to_blob(fig.to_html(), 'elbow_method_kmeans', storage_conn_str, container_name, folder='plots')