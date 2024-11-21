import sys
import pandas as pd
import plotly.express as px
import plotly.io as pio
from helper_functions import upload_to_blob, download_from_blob
import io

storage_conn_str = sys.argv[1]
container_name = sys.argv[2]
prefix = sys.argv[3] if len(sys.argv) > 3 else ''  # 'cleaned_' or no argument

columns = ['ID_Reserva', 'h_num_per', 'h_tot_hab', 'h_tfa_total', 'total_day', 'reservation_days']

filtered_df = download_from_blob(f'{prefix}filtered_df', storage_conn_str, container_name)

for column in columns:
    fig = px.line(filtered_df, x='Date', y=column, title=f'Time Series of {column} ({prefix})')
    
    plot_name = f'{prefix}time_series_{column}_plot'
    html_data = pio.to_html(fig, full_html=True)
    html_bytes = io.BytesIO(html_data.encode('utf-8'))

    upload_to_blob(html_bytes, plot_name, storage_conn_str, container_name, folder='plots')