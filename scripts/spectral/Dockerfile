FROM python:3.9-slim

WORKDIR /app

COPY scripts/spectral/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY scripts/spectral/helper_functions.py /app/helper_functions.py
COPY scripts/spectral/load_data.py /app/load_data.py
COPY scripts/spectral/scale_data.py /app/scale_data.py
COPY scripts/spectral/spectral_clustering.py /app/spectral_clustering.py
COPY scripts/spectral/plot_clusters.py /app/plot_clusters.py
COPY scripts/spectral/plot_pairplot.py /app/plot_pairplot.py
COPY scripts/spectral/plot_pca.py /app/plot_pca.py
COPY scripts/spectral/calculate_cluster_means.py /app/calculate_cluster_means.py

EXPOSE 8680