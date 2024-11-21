import sys
from helper_functions import upload_to_blob, download_from_blob
import io

storage_conn_str = sys.argv[1]
container_name = sys.argv[2]

grouped_df = download_from_blob(f'cleaned_filtered_df', storage_conn_str, container_name)
df = download_from_blob(f'cleaned_df', storage_conn_str, container_name)

name_model_data = 'model_data'
name_cleaned_rvs = 'cleaned_rvs'

upload_to_blob(grouped_df, name_model_data, storage_conn_str, container_name, folder='parquets')
upload_to_blob(df, name_cleaned_rvs, storage_conn_str, container_name, folder='parquets')