from azure.storage.blob import BlobServiceClient
import io
import pandas as pd
import pickle as pkl

def download_from_blob(filename, storage_conn_str, container_name, folder='temp_files'):
    blob_service_client = BlobServiceClient.from_connection_string(storage_conn_str)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=f'{folder}/{filename}.parquet')
    download_stream = blob_client.download_blob()
    df = pd.read_parquet(io.BytesIO(download_stream.readall()))
    return df

def upload_to_blob(df, filename, storage_conn_str, container_name, folder='temp_files'):
    if folder == 'plots':
        blob_service_client = BlobServiceClient.from_connection_string(storage_conn_str)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=f'{folder}/kmeans/{filename}.html')
        blob_client.upload_blob(df, overwrite=True)
    elif folder == 'pkls':
        pkl_buffer = io.BytesIO()
        pkl.dump(df, pkl_buffer)
        pkl_buffer.seek(0)

        blob_service_client = BlobServiceClient.from_connection_string(storage_conn_str)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=f'{folder}/{filename}.pkl')
        blob_client.upload_blob(pkl_buffer, overwrite=True)
    else:
        parquet_buffer = io.BytesIO()
        df.to_parquet(parquet_buffer)
        parquet_buffer.seek(0)

        blob_service_client = BlobServiceClient.from_connection_string(storage_conn_str)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=f'{folder}/{filename}.parquet')
        blob_client.upload_blob(parquet_buffer, overwrite=True)