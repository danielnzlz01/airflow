# Project Overview

This project includes Dockerfiles and requirements for various scripts, as well as functions for data loading, processing, and modeling using Apache Airflow.

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/danielnzlz01/airflow.git
    ```

2. Build the Docker images and start Airflow services:
    ```bash
    docker-compose up --build -d
    ```

3. To stop the Airflow services:
    ```bash
    docker-compose down
    ```

4. Access the Airflow web interface at `http://localhost:8080`.

5. To run the Streamlit dashboard (Once all plots and models are generated):
    ```bash
    docker-compose -f streamlit/docker-compose.yaml up --build -d
    ```

6. Access the Streamlit dashboard at `http://0.0.0.0:8585`.

7. To stop the Streamlit dashboard:
    ```bash
    docker-compose -f streamlit/docker-compose.yaml down
    ```

## IMPORTANT

If using linux, run the following commands to avoid database permission issues:

```bash
mkdir -p ./dags ./logs ./plugins ./config
echo -e "AIRFLOW_UID=$(id -u)" > .env
```

When Airflow GUI is accessed for the first time, it will ask for a password. The default username is `airflow` and the default password is `airflow`.

Set up Airflow connections and variables in the Airflow web interface.

For this project you need:

- An azure database connection string.
- An azure storage connection string.
- An azure container name.

The variables should be named as follows:

- `AZURE_DATABASE_CONNECTION_STRING:mssql+pymssql://<username>:<password>@<server>/<database>`
- `AZURE_STORAGE_CONNECTION_STRING:DefaultEndpointsProtocol=https;AccountName=<account_name>;AccountKey=<account_key>;EndpointSuffix=core.windows.net`
- `AZURE_CONTAINER_NAME:<container_name>`

These can be set up in a JSON file and then imported into the Airflow web interface.

## Directory Structure

- `config/`: Configuration files
- `logs/`: Log files
- `plugins/`: Custom plugins
- `dags/`: Directed Acyclic Graphs (DAGs) for Airflow
- `scripts/`: Various scripts pulled by DAGs

## Usage

1. Place your DAG files in the `dags/` directory.
2. Place your custom plugins in the `plugins/` directory.
3. Monitor the Airflow web interface to manage and trigger DAGs.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.
