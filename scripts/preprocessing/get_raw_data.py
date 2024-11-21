import pandas as pd
from sqlalchemy import create_engine
from helper_functions import upload_to_blob
import sys

table = 'reservaciones'

db_conn_str = sys.argv[1]
storage_conn_str = sys.argv[2]
container_name = sys.argv[3]

def get_raw_data(db_conn_str):
    engine = create_engine(f'{db_conn_str}')
    query = f"SELECT * FROM {table}"
    df = pd.read_sql(query, engine)

    # ID_Reserva                    int64
    # Fecha_hoy                    object
    # h_res_fec                     int64
    # h_res_fec_ok                 object
    # h_res_fec_okt                object
    # h_num_per                     int64
    # aa_h_num_per                  int64
    # h_num_adu                     int64
    # aa_h_num_adu                  int64
    # h_num_men                     int64
    # aa_h_num_men                  int64
    # h_num_noc                     int64
    # aa_h_num_noc                  int64
    # h_tot_hab                     int64
    # aa_h_tot_hab                  int64
    # ID_Programa                   int64
    # ID_Paquete                    int64
    # ID_Segmento_Comp              int64
    # ID_Agencia                    int64
    # ID_empresa                    int64
    # ID_Tipo_Habitacion            int64
    # ID_canal                      int64
    # h_fec_lld                    object
    # h_fec_lld_ok                 object
    # h_fec_lld_okt                object
    # h_fec_reg                    object
    # h_fec_reg_ok                 object
    # h_fec_reg_okt                object
    # h_fec_sda                    object
    # h_fec_sda_ok                 object
    # h_fec_sda_okt                object
    # ID_Pais_Origen                int64
    # Cliente_Disp                  int64
    # aa_Cliente_Disp               int64
    # Reservacion                   int64
    # aa_Reservacion                int64
    # ID_estatus_reservaciones      int64
    # h_can_res                    object
    # h_cod_reserva                object
    # h_edo                        object
    # h_codigop                    object
    # h_correo_e                   object
    # h_nom                        object
    # h_tfa_total                 float64
    # aa_h_tfa_total              float64
    # moneda_cve                    int64
    # h_ult_cam_fec                object
    # h_ult_cam_fec_ok             object
    # h_ult_cam_fec_okt            object

    df['ID_Reserva'] = df['ID_Reserva'].astype(int)
    df['Fecha_hoy'] = df['Fecha_hoy'].astype(str)
    df['h_res_fec'] = df['h_res_fec'].astype(int)
    df['h_res_fec_ok'] = df['h_res_fec_ok'].astype(str)
    df['h_res_fec_okt'] = df['h_res_fec_okt'].astype(str)
    df['h_num_per'] = df['h_num_per'].astype(int)
    df['aa_h_num_per'] = df['aa_h_num_per'].astype(int)
    df['h_num_adu'] = df['h_num_adu'].astype(int)
    df['aa_h_num_adu'] = df['aa_h_num_adu'].astype(int)
    df['h_num_men'] = df['h_num_men'].astype(int)
    df['aa_h_num_men'] = df['aa_h_num_men'].astype(int)
    df['h_num_noc'] = df['h_num_noc'].astype(int)
    df['aa_h_num_noc'] = df['aa_h_num_noc'].astype(int)
    df['h_tot_hab'] = df['h_tot_hab'].astype(int)
    df['aa_h_tot_hab'] = df['aa_h_tot_hab'].astype(int)
    df['ID_Programa'] = df['ID_Programa'].astype(int)
    df['ID_Paquete'] = df['ID_Paquete'].astype(int)
    df['ID_Segmento_Comp'] = df['ID_Segmento_Comp'].astype(int)
    df['ID_Agencia'] = df['ID_Agencia'].astype(int)
    df['ID_empresa'] = df['ID_empresa'].astype(int)
    df['ID_Tipo_Habitacion'] = df['ID_Tipo_Habitacion'].astype(int)
    df['ID_canal'] = df['ID_canal'].astype(int)
    df['h_fec_lld'] = df['h_fec_lld'].astype(str)
    df['h_fec_lld_ok'] = df['h_fec_lld_ok'].astype(str)
    df['h_fec_lld_okt'] = df['h_fec_lld_okt'].astype(str)
    df['h_fec_reg'] = df['h_fec_reg'].astype(str)
    df['h_fec_reg_ok'] = df['h_fec_reg_ok'].astype(str)
    df['h_fec_reg_okt'] = df['h_fec_reg_okt'].astype(str)
    df['h_fec_sda'] = df['h_fec_sda'].astype(str)
    df['h_fec_sda_ok'] = df['h_fec_sda_ok'].astype(str)
    df['h_fec_sda_okt'] = df['h_fec_sda_okt'].astype(str)
    df['ID_Pais_Origen'] = df['ID_Pais_Origen'].astype(int)
    df['Cliente_Disp'] = df['Cliente_Disp'].astype(int)
    df['aa_Cliente_Disp'] = df['aa_Cliente_Disp'].astype(int)
    df['Reservacion'] = df['Reservacion'].astype(int)
    df['aa_Reservacion'] = df['aa_Reservacion'].astype(int)
    df['ID_estatus_reservaciones'] = df['ID_estatus_reservaciones'].astype(int)
    df['h_can_res'] = df['h_can_res'].astype(str)
    df['h_cod_reserva'] = df['h_cod_reserva'].astype(str)
    df['h_edo'] = df['h_edo'].astype(str)
    df['h_codigop'] = df['h_codigop'].astype(str)
    df['h_correo_e'] = df['h_correo_e'].astype(str)
    df['h_nom'] = df['h_nom'].astype(str)
    df['h_tfa_total'] = df['h_tfa_total'].astype(float)
    df['aa_h_tfa_total'] = df['aa_h_tfa_total'].astype(float)
    df['moneda_cve'] = df['moneda_cve'].astype(int)
    df['h_ult_cam_fec'] = df['h_ult_cam_fec'].astype(str)
    df['h_ult_cam_fec_ok'] = df['h_ult_cam_fec_ok'].astype(str)
    df['h_ult_cam_fec_okt'] = df['h_ult_cam_fec_okt'].astype(str)

    upload_to_blob(df, 'raw_data', storage_conn_str, container_name)

if __name__ == "__main__":
    get_raw_data(db_conn_str)