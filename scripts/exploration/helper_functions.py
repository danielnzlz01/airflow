from azure.storage.blob import BlobServiceClient
import io
import pandas as pd

def download_from_blob(filename, storage_conn_str, container_name, folder='temp_files'):
    blob_service_client = BlobServiceClient.from_connection_string(storage_conn_str)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=f'{folder}/{filename}.parquet')
    download_stream = blob_client.download_blob()
    df = pd.read_parquet(io.BytesIO(download_stream.readall()))
    return df

def upload_to_blob(df, filename, storage_conn_str, container_name, folder='temp_files'):
    if folder == 'plots':
        blob_service_client = BlobServiceClient.from_connection_string(storage_conn_str)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=f'{folder}/exploration/{filename}.html')
        blob_client.upload_blob(df, overwrite=True)
    else:
        parquet_buffer = io.BytesIO()
        df.to_parquet(parquet_buffer, index=False)
        parquet_buffer.seek(0)

        blob_service_client = BlobServiceClient.from_connection_string(storage_conn_str)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=f'{folder}/{filename}.parquet')
        blob_client.upload_blob(parquet_buffer, overwrite=True)