from airflow import DAG
from datetime import datetime, timedelta

args = {
    'owner': 'coder2j',
    'retries': 3,
    'retry_delay' : timedelta(minutes= 2)
}





with DAG(
    default_args = args,
    dag_id = 'our_dag_with_python_operator_v01',
    description = 'Our first dag using python operator',
    start_date = datetime(2021, 10, 6),
    schedule_interval = '@daily'
) as dag: