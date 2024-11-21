import sys
from helper_functions import download_from_blob, upload_to_blob

storage_conn_str = sys.argv[1]
container_name = sys.argv[2]
table = 'reservaciones_expandido'
folder = 'parquets'

df = download_from_blob(table, storage_conn_str, container_name, folder)

upload_to_blob(df, 'df', storage_conn_str, container_name)