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
    description = "practicing will make different!",
    start_date = datetime(2024, 10, 28, 6),
    schedule_interal = '@daily'
) as dag:
    pass