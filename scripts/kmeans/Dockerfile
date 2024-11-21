FROM python:3.9-slim

WORKDIR /app

COPY scripts/kmeans/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY scripts/kmeans/helper_functions.py /app/helper_functions.py
COPY scripts/kmeans/load_data.py /app/load_data.py
COPY scripts/kmeans/scale_data.py /app/scale_data.py
COPY scripts/kmeans/plot_elbow_curve.py /app/plot_elbow_curve.py
COPY scripts/kmeans/fit_kmeans.py /app/fit_kmeans.py
COPY scripts/kmeans/plot_clusters.py /app/plot_clusters.py
COPY scripts/kmeans/plot_pairplot.py /app/plot_pairplot.py
COPY scripts/kmeans/plot_pca.py /app/plot_pca.py
COPY scripts/kmeans/calculate_cluster_means.py /app/calculate_cluster_means.py

EXPOSE 8480