from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

args = {
    'owner': 'saferoom',
    'retries': 3,
    'retry_delay': timedelta(minutes = 2)
}