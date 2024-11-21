from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime
from airflow.models import Variable

storage_conn_str = Variable.get('AZURE_STORAGE_CONNECTION_STRING')
container_name = Variable.get('AZURE_CONTAINER_NAME')

with DAG(
    dag_id='kmeans_dag',
    start_date=datetime(2024, 11, 16),
    schedule_interval='@daily',
    catchup=False,
) as dag:
    load_data_task = DockerOperator(
        task_id='load_data',
        image='airflow-kmeans:latest',
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

    scale_data_task = DockerOperator(
        task_id='scale_data',
        image='airflow-kmeans:latest',
        api_version='auto',
        auto_remove=True,
        command=f'python scale_data.py {storage_conn_str} {container_name}',
        docker_url='unix://var/run/docker.sock',
        mount_tmp_dir=False,
        environment={
            'AZURE_STORAGE_CONNECTION_STRING': storage_conn_str,
            'CONTAINER_NAME': container_name
        }
    )

    fit_kmeans_task = DockerOperator(
        task_id='fit_kmeans',
        image='airflow-kmeans:latest',
        api_version='auto',
        auto_remove=True,
        command=f'python fit_kmeans.py {storage_conn_str} {container_name}',
        docker_url='unix://var/run/docker.sock',
        mount_tmp_dir=False,
        environment={
            'AZURE_STORAGE_CONNECTION_STRING': storage_conn_str,
            'CONTAINER_NAME': container_name
        }
    )

    calculate_cluster_means_task = DockerOperator(
        task_id='calculate_cluster_means',
        image='airflow-kmeans:latest',
        api_version='auto',
        auto_remove=True,
        command=f'python calculate_cluster_means.py {storage_conn_str} {container_name}',
        docker_url='unix://var/run/docker.sock',
        mount_tmp_dir=False,
        environment={
            'AZURE_STORAGE_CONNECTION_STRING': storage_conn_str,
            'CONTAINER_NAME': container_name
        }
    )

    plot_clusters_task = DockerOperator(
        task_id='plot_clusters',
        image='airflow-kmeans:latest',
        api_version='auto',
        auto_remove=True,
        command=f'python plot_clusters.py {storage_conn_str} {container_name}',
        docker_url='unix://var/run/docker.sock',
        mount_tmp_dir=False,
        environment={
            'AZURE_STORAGE_CONNECTION_STRING': storage_conn_str,
            'CONTAINER_NAME': container_name
        }
    )

    plot_elbow_curve_task = DockerOperator(
        task_id='plot_elbow_curve',
        image='airflow-kmeans:latest',
        api_version='auto',
        auto_remove=True,
        command=f'python plot_elbow_curve.py {storage_conn_str} {container_name}',
        docker_url='unix://var/run/docker.sock',
        mount_tmp_dir=False,
        environment={
            'AZURE_STORAGE_CONNECTION_STRING': storage_conn_str,
            'CONTAINER_NAME': container_name
        }
    )

    plot_pairplot_task = DockerOperator(
        task_id='plot_pairplot',
        image='airflow-kmeans:latest',
        api_version='auto',
        auto_remove=True,
        command=f'python plot_pairplot.py {storage_conn_str} {container_name}',
        docker_url='unix://var/run/docker.sock',
        mount_tmp_dir=False,
        environment={
            'AZURE_STORAGE_CONNECTION_STRING': storage_conn_str,
            'CONTAINER_NAME': container_name
        }
    )

    plot_pca_task = DockerOperator(
        task_id='plot_pca',
        image='airflow-kmeans:latest',
        api_version='auto',
        auto_remove=True,
        command=f'python plot_pca.py {storage_conn_str} {container_name}',
        docker_url='unix://var/run/docker.sock',
        mount_tmp_dir=False,
        environment={
            'AZURE_STORAGE_CONNECTION_STRING': storage_conn_str,
            'CONTAINER_NAME': container_name
        }
    )

load_data_task >> scale_data_task >> fit_kmeans_task >> [plot_clusters_task, plot_elbow_curve_task, plot_pairplot_task, plot_pca_task] >> calculate_cluster_means_task
