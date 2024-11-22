import plotly.figure_factory as ff
from scipy.cluster.hierarchy import linkage
from helper_functions import download_from_blob, upload_to_blob
import sys

storage_conn_str = sys.argv[1]
container_name = sys.argv[2]

data_scaled = download_from_blob('scaled_df_hierarchical', storage_conn_str, container_name)

linked = linkage(data_scaled, method = 'ward')

fig = ff.create_dendrogram(linked, orientation='bottom')
fig.update_layout(title='Hierarchical Clustering Dendrogram', yaxis_title='Distance', xaxis=dict(showline=True, showgrid=False, showticklabels=False))
upload_to_blob(fig.to_html(), 'dendrogram_hierarchical', storage_conn_str, container_name, folder='plots')