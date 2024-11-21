FROM python:3.9-slim

WORKDIR /app

COPY scripts/hierarchical/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY scripts/hierarchical/helper_functions.py /app/helper_functions.py
COPY scripts/hierarchical/load_data.py /app/load_data.py
COPY scripts/hierarchical/scale_data.py /app/scale_data.py
COPY scripts/hierarchical/agglomerative_clustering.py /app/agglomerative_clustering.py
COPY scripts/hierarchical/plot_clusters.py /app/plot_clusters.py
COPY scripts/hierarchical/plot_pairplot.py /app/plot_pairplot.py
COPY scripts/hierarchical/plot_pca.py /app/plot_pca.py
COPY scripts/hierarchical/plot_dendogram.py /app/plot_dendogram.py
COPY scripts/hierarchical/calculate_cluster_means.py /app/calculate_cluster_means.py

EXPOSE 8580