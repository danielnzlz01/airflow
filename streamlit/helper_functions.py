from azure.storage.blob import BlobServiceClient
import io
import pandas as pd

def download_from_blob(filename, storage_conn_str, container_name, folder='temp_files', subfolder=None):
    if folder == 'plots':
        blob_service_client = BlobServiceClient.from_connection_string(storage_conn_str)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=f'{folder}/{subfolder}/{filename}.html')
        download_stream = blob_client.download_blob()
        html_content = download_stream.readall()
        return html_content
    else:
        blob_service_client = BlobServiceClient.from_connection_string(storage_conn_str)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=f'{folder}/{filename}.parquet')
        download_stream = blob_client.download_blob()
        df = pd.read_parquet(io.BytesIO(download_stream.readall()))
        return df