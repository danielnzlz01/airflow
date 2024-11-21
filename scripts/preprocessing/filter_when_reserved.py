from helper_functions import download_from_blob, upload_to_blob
import sys

storage_conn_str = sys.argv[1]
container_name = sys.argv[2]

def filter_when_reserved():
    df = download_from_blob('raw_data', storage_conn_str, container_name)
    df = df[df['Reservacion'] == 1]
    upload_to_blob(df, 'filtered_reserved', storage_conn_str, container_name)

if __name__ == "__main__":
    filter_when_reserved()