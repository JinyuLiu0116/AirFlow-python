from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

args = {
    'owner': 'Postgres',
    'retries': 3,
    'retry_delay': timedelta(minutes = 2)
}


with DAG(
    


) as dag:
    pass