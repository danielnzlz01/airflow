import pandas as pd
from helper_functions import download_from_blob, upload_to_blob
import sys

storage_conn_str = sys.argv[1]
container_name = sys.argv[2]

def convert_data_types():
    df = download_from_blob('filtered_columns', storage_conn_str, container_name)
    df['ID_Reserva'] = df['ID_Reserva'].astype(str)
    df['h_res_fec_ok'] = pd.to_datetime(df['h_res_fec_ok'])
    df['h_fec_lld_ok'] = pd.to_datetime(df['h_fec_lld_ok'])
    df['h_fec_reg_ok'] = pd.to_datetime(df['h_fec_reg_ok'])
    df['h_fec_sda_ok'] = pd.to_datetime(df['h_fec_sda_ok'])

    upload_to_blob(df, 'converted_data_types', storage_conn_str, container_name)

if __name__ == "__main__":
    convert_data_types()

# docker build -f scripts/preprocessing/Dockerfile -t preprocessing .
# docker build -f scripts/exploration/Dockerfile -t exploration .
# docker build -f scripts/model1/Dockerfile -t model1 .
# docker compose up --build -d
# docker compose down