import sys
import pandas as pd
from helper_functions import download_from_blob, upload_to_blob

storage_conn_str = sys.argv[1]
container_name = sys.argv[2]
prefix = sys.argv[3] if len(sys.argv) > 3 else '' # 'cleaned_' or no argument

df = download_from_blob(f'{prefix}df', storage_conn_str, container_name)

df['Date'] = pd.to_datetime(df['Date'])

# df['ID_Reserva'] = df['ID_Reserva'].astype(int)
# df['h_num_per'] = df['h_num_per'].astype(int)
# df['h_tot_hab'] = df['h_tot_hab'].astype(int)
# df['h_tfa_total'] = df['h_tfa_total'].astype(float)
# df['total_day'] = df['total_day'].astype(float)
# df['reservation_days'] = df['reservation_days'].astype(float)

grouped_df = df.groupby('Date').agg({
    'ID_Reserva': 'count',
    'h_tfa_total': 'mean',  
    'h_num_per' : 'mean',
    'h_tot_hab' : 'mean',
    'h_tfa_total' : 'mean',
    'total_day' : 'mean',
    'reservation_days' : 'mean'
}).reset_index()
grouped_df = grouped_df.sort_values('Date')

upload_to_blob(grouped_df, f'{prefix}grouped_df', storage_conn_str, container_name)