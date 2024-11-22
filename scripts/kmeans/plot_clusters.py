import sys
from helper_functions import download_from_blob, upload_to_blob
import plotly.express as px

storage_conn_str = sys.argv[1]
container_name = sys.argv[2]

df = download_from_blob('clusters_kmeans', storage_conn_str, container_name, folder='parquets')
df['Cluster'] = df['Cluster'].astype(str)
fig = px.scatter(df, y='ID_Reserva', color='Cluster', title='Reservations by Date and K-means Cluster')
fig.update_layout(
    xaxis_title='Date',
    yaxis_title='Reservation ID'
)
fig.update_traces(mode='lines+markers')
upload_to_blob(fig.to_html(), 'reservations_date_cluster_kmeans', storage_conn_str, container_name, folder='plots')

