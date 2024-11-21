from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime
from airflow.models import Variable

storage_conn_str = Variable.get('AZURE_STORAGE_CONNECTION_STRING')
container_name = Variable.get('AZURE_CONTAINER_NAME')

with DAG(
    dag_id='data_exploration_dag',
    start_date=datetime(2024, 11, 16),
    schedule_interval='@daily',
    catchup=False,
) as dag:
    load_data_task = DockerOperator(
        task_id='load_data',
        image='airflow-exploration:latest',
        api_version='auto',
        auto_remove=True,
        command=f'python load_data.py {storage_conn_str} {container_name}',
        docker_url='unix://var/run/docker.sock',
        mount_tmp_dir=False,
        environment={
            'AZURE_STORAGE_CONNECTION_STRING': storage_conn_str,
            'CONTAINER_NAME': container_name
        }
    )

    group_data_task = DockerOperator(
        task_id='group_data',
        image='airflow-exploration:latest',
        api_version='auto',
        auto_remove=True,
        command=f'python group_data.py {storage_conn_str} {container_name}',
        docker_url='unix://var/run/docker.sock',
        mount_tmp_dir=False,
        environment={
            'AZURE_STORAGE_CONNECTION_STRING': storage_conn_str,
            'CONTAINER_NAME': container_name
        }
    )

    filter_data_task = DockerOperator(
        task_id='filter_data',
        image='airflow-exploration:latest',
        api_version='auto',
        auto_remove=True,
        command=f'python filter_data.py {storage_conn_str} {container_name}',
        docker_url='unix://var/run/docker.sock',
        mount_tmp_dir=False,
        environment={
            'AZURE_STORAGE_CONNECTION_STRING': storage_conn_str,
            'CONTAINER_NAME': container_name
        }
    )

    plot_reservations_task = DockerOperator(
        task_id='plot_reservations',
        image='airflow-exploration:latest',
        api_version='auto',
        auto_remove=True,
        command=f'python plot_reservations.py {storage_conn_str} {container_name}',
        docker_url='unix://var/run/docker.sock',
        mount_tmp_dir=False,
        environment={
            'AZURE_STORAGE_CONNECTION_STRING': storage_conn_str,
            'CONTAINER_NAME': container_name
        }
    )

    plot_correlation_matrix_task = DockerOperator(
        task_id='plot_correlation_matrix',
        image='airflow-exploration:latest',
        api_version='auto',
        auto_remove=True,
        command=f'python plot_correlation_matrix.py {storage_conn_str} {container_name}',
        docker_url='unix://var/run/docker.sock',
        mount_tmp_dir=False,
        environment={
            'AZURE_STORAGE_CONNECTION_STRING': storage_conn_str,
            'CONTAINER_NAME': container_name
        }
    )

    plot_time_series_task = DockerOperator(
        task_id='plot_time_series',
        image='airflow-exploration:latest',
        api_version='auto',
        auto_remove=True,
        command=f'python plot_time_series.py {storage_conn_str} {container_name}',
        docker_url='unix://var/run/docker.sock',
        mount_tmp_dir=False,
        environment={
            'AZURE_STORAGE_CONNECTION_STRING': storage_conn_str,
            'CONTAINER_NAME': container_name
        }
    )

    clean_data_task = DockerOperator(
        task_id='clean_data',
        image='airflow-exploration:latest',
        api_version='auto',
        auto_remove=True,
        command=f'python clean_data.py {storage_conn_str} {container_name}',
        docker_url='unix://var/run/docker.sock',
        mount_tmp_dir=False,
        environment={
            'AZURE_STORAGE_CONNECTION_STRING': storage_conn_str,
            'CONTAINER_NAME': container_name
        }
    )

    plot_boxplots_task = DockerOperator(
        task_id='plot_boxplots',
        image='airflow-exploration:latest',
        api_version='auto',
        auto_remove=True,
        command=f'python plot_boxplots.py {storage_conn_str} {container_name}',
        docker_url='unix://var/run/docker.sock',
        mount_tmp_dir=False,
        environment={
            'AZURE_STORAGE_CONNECTION_STRING': storage_conn_str,
            'CONTAINER_NAME': container_name
        }
    )

    group_data_cleaned_task = DockerOperator(
        task_id='group_data_cleaned',
        image='airflow-exploration:latest',
        api_version='auto',
        auto_remove=True,
        command=f'python group_data.py {storage_conn_str} {container_name} cleaned_',
        docker_url='unix://var/run/docker.sock',
        mount_tmp_dir=False,
        environment={
            'AZURE_STORAGE_CONNECTION_STRING': storage_conn_str,
            'CONTAINER_NAME': container_name
        }
    )

    filter_data_cleaned_task = DockerOperator(
        task_id='filter_data_cleaned',
        image='airflow-exploration:latest',
        api_version='auto',
        auto_remove=True,
        command=f'python filter_data.py {storage_conn_str} {container_name} cleaned_',
        docker_url='unix://var/run/docker.sock',
        mount_tmp_dir=False,
        environment={
            'AZURE_STORAGE_CONNECTION_STRING': storage_conn_str,
            'CONTAINER_NAME': container_name
        }
    )

    plot_time_series_cleaned_task = DockerOperator(
        task_id='plot_time_series_cleaned',
        image='airflow-exploration:latest',
        api_version='auto',
        auto_remove=True,
        command=f'python plot_time_series.py {storage_conn_str} {container_name} cleaned_',
        docker_url='unix://var/run/docker.sock',
        mount_tmp_dir=False,
        environment={
            'AZURE_STORAGE_CONNECTION_STRING': storage_conn_str,
            'CONTAINER_NAME': container_name
        }
    )

    plot_correlation_matrix_cleaned_task = DockerOperator(
        task_id='plot_correlation_matrix_cleaned',
        image='airflow-exploration:latest',
        api_version='auto',
        auto_remove=True,
        command=f'python plot_correlation_matrix.py {storage_conn_str} {container_name} cleaned_',
        docker_url='unix://var/run/docker.sock',
        mount_tmp_dir=False,
        environment={
            'AZURE_STORAGE_CONNECTION_STRING': storage_conn_str,
            'CONTAINER_NAME': container_name
        }
    )

    save_data_task = DockerOperator(
        task_id='save_data',
        image='airflow-exploration:latest',
        api_version='auto',
        auto_remove=True,
        command=f'python save_data.py {storage_conn_str} {container_name}',
        docker_url='unix://var/run/docker.sock',
        mount_tmp_dir=False,
        environment={
            'AZURE_STORAGE_CONNECTION_STRING': storage_conn_str,
            'CONTAINER_NAME': container_name
        }
    )


load_data_task >> group_data_task >> filter_data_task >> [plot_reservations_task, plot_correlation_matrix_task, plot_time_series_task]
load_data_task >> clean_data_task >> plot_boxplots_task >> group_data_cleaned_task >> filter_data_cleaned_task >> [plot_time_series_cleaned_task, plot_correlation_matrix_cleaned_task] >> save_data_task
