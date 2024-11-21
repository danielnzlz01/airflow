FROM python:3.9-slim

WORKDIR /app

COPY scripts/mapper/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY scripts/mapper/helper_functions.py /app/helper_functions.py
COPY scripts/mapper/load_data.py /app/load_data.py
COPY scripts/mapper/scale_data.py /app/scale_data.py
COPY scripts/mapper/plot_mapper.py /app/plot_mapper.py

EXPOSE 8780