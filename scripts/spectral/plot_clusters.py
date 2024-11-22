import sys
from helper_functions import download_from_blob, upload_to_blob
import plotly.express as px
import pandas as pd
import numpy as np

storage_conn_str = sys.argv[1]
container_name = sys.argv[2]

data = download_from_blob('spectral_data_cluster', storage_conn_str, container_name)
threshold = pd.Timedelta(days=30)
data['Gap'] = (
    data.groupby('Cluster').apply(
        lambda group: group.index.to_series().diff() > threshold
    ).reset_index(level=0, drop=True)
)
data.loc[data['Gap'], 'ID_Reserva'] = np.nan
fig= px.scatter(data, x=data.index, y='ID_Reserva', color='Cluster', title='Reservations by Date and Cluster for Spectral Clustering')
fig.update_layout(
    xaxis_title='Date',
    yaxis_title='Reservation ID'
)
fig.update_traces(mode='lines+markers')

upload_to_blob(fig.to_html(), 'reservations_date_cluster_spectral', storage_conn_str, container_name, folder='plots')