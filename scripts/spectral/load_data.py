import sys
from helper_functions import download_from_blob, upload_to_blob
import pandas as pd

storage_conn_str = sys.argv[1]
container_name = sys.argv[2]

df = download_from_blob('model_data', storage_conn_str, container_name, folder='parquets')
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

upload_to_blob(df, 'spectral_data', storage_conn_str, container_name)