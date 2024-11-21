import sys
import pandas as pd
from helper_functions import download_from_blob, upload_to_blob

storage_conn_str = sys.argv[1]
container_name = sys.argv[2]
prefix = sys.argv[3] if len(sys.argv) > 3 else ''  # 'cleaned_' or no argument

grouped_df = download_from_blob(f'{prefix}grouped_df', storage_conn_str, container_name)

filtered_df = grouped_df[grouped_df['ID_Reserva'] > 80]

upload_to_blob(filtered_df, f'{prefix}filtered_df', storage_conn_str, container_name)