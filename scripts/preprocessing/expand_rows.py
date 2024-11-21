import pandas as pd
from helper_functions import download_from_blob, upload_to_blob
import sys

storage_conn_str = sys.argv[1]
container_name = sys.argv[2]

def expand_rows():
    df = download_from_blob('extra_columns', storage_conn_str, container_name)
    expanded_df = df.apply(lambda row: pd.DataFrame({
        'Date': pd.date_range(row['h_fec_lld_ok'], row['h_fec_sda_ok']),
        'ID_Reserva': row['ID_Reserva'],
        'h_num_per': row['h_num_per'],
        'h_tot_hab': row['h_tot_hab'],
        'h_can_res': row['h_can_res'],
        'h_tfa_total': row['h_tfa_total'],
        'total_day': row['total_day'],
        'reservation_days': row['reservation_days']
    }), axis=1)
    expanded_df = pd.concat(expanded_df.values).reset_index(drop=True)
    upload_to_blob(expanded_df, 'reservaciones_expandido', storage_conn_str, container_name, folder)

if __name__ == "__main__":
    folder = 'parquets'
    expand_rows()