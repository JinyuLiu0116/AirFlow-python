from airflow import DAG
from datetime import datetime, timedelta

args = {
    'owner': 'room',
    'retries': 3,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id = "repeat_dag_untill_familiar",
    default_args = args,
) as dag:
    pass