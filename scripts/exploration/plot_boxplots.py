import sys
import pandas as pd
import plotly.express as px
import plotly.io as pio
from helper_functions import upload_to_blob, download_from_blob
import io

storage_conn_str = sys.argv[1]
container_name = sys.argv[2]
columns = ['ID_Reserva', 'h_num_per', 'h_tot_hab', 'h_tfa_total', 'total_day', 'reservation_days']

df = download_from_blob('cleaned_df', storage_conn_str, container_name)

for column in columns:
    fig = px.box(df, y=column, title=f'Boxplot of {column} (Cleaned)')
    
    plot_name = f'cleaned_boxplot_{column}_plot'
    html_data = pio.to_html(fig, full_html=True)
    html_bytes = io.BytesIO(html_data.encode('utf-8'))

    upload_to_blob(html_bytes, plot_name, storage_conn_str, container_name, folder='plots')