FROM python:3.9-slim

WORKDIR /app

COPY scripts/exploration/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY scripts/exploration/helper_functions.py /app/helper_functions.py
COPY scripts/exploration/load_data.py /app/load_data.py
COPY scripts/exploration/group_data.py /app/group_data.py
COPY scripts/exploration/filter_data.py /app/filter_data.py
COPY scripts/exploration/plot_reservations.py /app/plot_reservations.py
COPY scripts/exploration/plot_correlation_matrix.py /app/plot_correlation_matrix.py
COPY scripts/exploration/plot_time_series.py /app/plot_time_series.py
COPY scripts/exploration/clean_data.py /app/clean_data.py
COPY scripts/exploration/plot_boxplots.py /app/plot_boxplots.py
COPY scripts/exploration/save_data.py /app/save_data.py

EXPOSE 8380