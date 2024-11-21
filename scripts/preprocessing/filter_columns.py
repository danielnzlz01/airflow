from helper_functions import download_from_blob, upload_to_blob
import sys

storage_conn_str = sys.argv[1]
container_name = sys.argv[2]

def filter_columns():
    df = download_from_blob('filtered_reserved', storage_conn_str, container_name)
    columns = ['ID_Reserva', 'h_res_fec_ok', 'h_num_per', 'h_tot_hab', 'h_fec_lld_ok', 'h_fec_reg_ok', 'h_fec_sda_ok', 'h_can_res', 'h_tfa_total']
    df = df[columns]
    upload_to_blob(df, 'filtered_columns', storage_conn_str, container_name)

if __name__ == "__main__":
    filter_columns()