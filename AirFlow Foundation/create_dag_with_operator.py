from airflow import DAG
from datetime import datetime, timedelta

args = {
    'owner': 'coder2j',
    'retries': 3,
    'retry_delay' : timedelta(minutes= 2)
}

with DAG(

) as dag: