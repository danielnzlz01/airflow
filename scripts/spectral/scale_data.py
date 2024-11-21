import sys
from helper_functions import download_from_blob, upload_to_blob
from sklearn.preprocessing import StandardScaler
import pandas as pd

storage_conn_str = sys.argv[1]
container_name = sys.argv[2]

df = download_from_blob('spectral_data', storage_conn_str, container_name)
scaler = StandardScaler()
data_scaled = scaler.fit_transform(df)
scaled_df = pd.DataFrame(data_scaled, columns=df.columns)
upload_to_blob(scaled_df, 'scaled_df_spectral', storage_conn_str, container_name)