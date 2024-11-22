FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app.py /app/app.py
COPY helper_functions.py /app/helper_functions.py

EXPOSE 8585

CMD ["streamlit", "run", "app.py", "--server.port=8585"]