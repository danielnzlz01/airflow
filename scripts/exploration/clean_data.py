import sys
from helper_functions import download_from_blob, upload_to_blob
import pandas as pd

storage_conn_str = sys.argv[1]
container_name = sys.argv[2]

df = download_from_blob('df', storage_conn_str, container_name)

# df['ID_Reserva'] = df['ID_Reserva'].astype(int)
# df['h_num_per'] = df['h_num_per'].astype(int)
# df['h_tot_hab'] = df['h_tot_hab'].astype(int)
# df['h_tfa_total'] = df['h_tfa_total'].astype(float)
# df['total_day'] = df['total_day'].astype(float)
# df['reservation_days'] = df['reservation_days'].astype(float)

data = df[df['h_tot_hab'] > 0]
data = data[data['reservation_days'] < 600]
df = df[df['reservation_days'] >= 0]

mean_tfa = df['h_tfa_total'].mean()
std_tfa = df['h_tfa_total'].std()
df = df[df['h_tfa_total'] < mean_tfa + 5*std_tfa]

mean_total_day = df['total_day'].mean()
std_total_day = df['total_day'].std()
df = df[df['total_day'] < mean_total_day + 5*std_total_day]

mean_res_days = df['reservation_days'].mean()
std_res_days = df['reservation_days'].std()
df = df[df['reservation_days'] < mean_res_days + 5*std_res_days]

upload_to_blob(df, 'cleaned_df', storage_conn_str, container_name, folder='temp_files')