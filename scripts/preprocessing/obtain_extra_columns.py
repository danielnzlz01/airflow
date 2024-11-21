from helper_functions import download_from_blob, upload_to_blob
import sys

storage_conn_str = sys.argv[1]
container_name = sys.argv[2]

def obtain_extra_columns():
    df = download_from_blob('converted_data_types', storage_conn_str, container_name)
    df['total_day'] = (df['h_fec_sda_ok'] - df['h_fec_lld_ok']).dt.days
    df['reservation_days'] = (df['h_fec_lld_ok'] - df['h_fec_reg_ok']).dt.days
    upload_to_blob(df, 'extra_columns', storage_conn_str, container_name)

if __name__ == "__main__":
    obtain_extra_columns()