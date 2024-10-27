from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

args = {
    'owner' : 'coder2j',
    'retries' : 3,
    'retry_delay' : timedelta(minutes=1)
}


with DAG(
    dag_id = 'our_first_dag',
    default_args = args,
    description = 'This is our first dag that wewrite',
    start_date = datetime(2024, 10, 27, 2),
    schedule_interval = '@daily'

) as dag:
    task1 = BashOperator(
        task_id = 'first_task',
        bash_command = "echo hello world, this is our first task!"
    )
    task2 = BashOperator(
        task_id = 'second_task',
        bash_command = "echo hello world, this is our second task!"
    )

    task1.set_downstream(task2)
