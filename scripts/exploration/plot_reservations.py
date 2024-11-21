import sys
import pandas as pd
import plotly.express as px
import plotly.io as pio
from helper_functions import upload_to_blob, download_from_blob
import io

storage_conn_str = sys.argv[1]
container_name = sys.argv[2]

df = download_from_blob('filtered_df', storage_conn_str, container_name)

fig = px.line(df, x='Date', y='ID_Reserva', title=f'Number of Reservations by Day (Filtered > 80)')

plot_name = f'filtered_reservations_plot'
html_data = pio.to_html(fig, full_html=True)
html_bytes = io.BytesIO(html_data.encode('utf-8'))

upload_to_blob(html_bytes, plot_name, storage_conn_str, container_name, folder='plots')