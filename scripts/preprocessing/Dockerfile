FROM python:3.9-slim

WORKDIR /app

COPY scripts/preprocessing/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY scripts/preprocessing/helper_functions.py /app/helper_functions.py
COPY scripts/preprocessing/get_raw_data.py /app/get_raw_data.py
COPY scripts/preprocessing/filter_when_reserved.py /app/filter_when_reserved.py
COPY scripts/preprocessing/filter_columns.py /app/filter_columns.py
COPY scripts/preprocessing/convert_data_types.py /app/convert_data_types.py
COPY scripts/preprocessing/obtain_extra_columns.py /app/obtain_extra_columns.py
COPY scripts/preprocessing/expand_rows.py /app/expand_rows.py

EXPOSE 8280

# to build use the following command
# docker build -f scripts/preprocessing/Dockerfile -t preprocessing .
# to run use the following command
# docker run -p 8280:8280 preprocessing
# docker run -p 8280:8280 --env-file path/to/.env preprocessing
# docker run --rm -it --env-file scripts/preprocessing/.env preprocessing python get_raw_data.py