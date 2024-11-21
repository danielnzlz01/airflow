from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime
from airflow.models import Variable

db_conn_str = Variable.get('AZURE_DATABASE_CONNECTION_STRING')
container_name = Variable.get('AZURE_CONTAINER_NAME')
storage_conn_str = Variable.get('AZURE_STORAGE_CONNECTION_STRING')

with DAG(
    dag_id='data_preprocessing_dag',
    start_date=datetime(2024, 11, 16),
    schedule_interval='@daily',
    catchup=False,
) as dag:
    get_raw_data_task = DockerOperator(
        task_id='get_raw_data',
        image='airflow-preprocessing:latest',
        api_version='auto',
        auto_remove=True,
        command=f'python get_raw_data.py {db_conn_str} {storage_conn_str} {container_name}',
        docker_url='unix://var/run/docker.sock',
        mount_tmp_dir=False,
        environment={
            'AZURE_DATABASE_CONNECTION_STRING': db_conn_str,
            'CONTAINER_NAME': container_name,
            'AZURE_STORAGE_CONNECTION_STRING': storage_conn_str
        }
    )

    filter_when_reserved_task = DockerOperator(
        task_id='filter_when_reserved',
        image='airflow-preprocessing:latest',
        api_version='auto',
        auto_remove=True,
        command=f'python filter_when_reserved.py {storage_conn_str} {container_name}',
        docker_url='unix://var/run/docker.sock',
        mount_tmp_dir=False,
        environment={
            'CONTAINER_NAME': container_name,
            'AZURE_STORAGE_CONNECTION_STRING': storage_conn_str
        }
    )

    filter_columns_task = DockerOperator(
        task_id='filter_columns',
        image='airflow-preprocessing:latest',
        api_version='auto',
        auto_remove=True,
        command=f'python filter_columns.py {storage_conn_str} {container_name}',
        docker_url='unix://var/run/docker.sock',
        mount_tmp_dir=False,
        environment={
            'CONTAINER_NAME': container_name,
            'AZURE_STORAGE_CONNECTION_STRING': storage_conn_str
        }
    )

    convert_data_types_task = DockerOperator(
        task_id='convert_data_types',
        image='airflow-preprocessing:latest',
        api_version='auto',
        auto_remove=True,
        command=f'python convert_data_types.py {storage_conn_str} {container_name}',
        docker_url='unix://var/run/docker.sock',
        mount_tmp_dir=False,
        environment={
            'CONTAINER_NAME': container_name,
            'AZURE_STORAGE_CONNECTION_STRING': storage_conn_str
        }
    )

    obtain_extra_columns_task = DockerOperator(
        task_id='obtain_extra_columns',
        image='airflow-preprocessing:latest',
        api_version='auto',
        auto_remove=True,
        command=f'python obtain_extra_columns.py {storage_conn_str} {container_name}',
        docker_url='unix://var/run/docker.sock',
        mount_tmp_dir=False,
        environment={
            'CONTAINER_NAME': container_name,
            'AZURE_STORAGE_CONNECTION_STRING': storage_conn_str
        }
    )

    expand_rows_task = DockerOperator(
        task_id='expand_rows',
        image='airflow-preprocessing:latest',
        api_version='auto',
        auto_remove=True,
        command=f'python expand_rows.py {storage_conn_str} {container_name}',
        docker_url='unix://var/run/docker.sock',
        mount_tmp_dir=False,
        environment={
            'CONTAINER_NAME': container_name,
            'AZURE_STORAGE_CONNECTION_STRING': storage_conn_str
        }
    )

get_raw_data_task >> filter_when_reserved_task >> filter_columns_task >> convert_data_types_task >> obtain_extra_columns_task >> expand_rows_task