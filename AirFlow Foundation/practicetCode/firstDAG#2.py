from airflow import DAG
from airflow.operators.bash import BashOperator
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
    task1 = BashOperator(
        task_id = 'first_task',
        bash_command = "Hello world another day!"
    )
    task2 = BashOperator(
        task_id = 'second_task',
        bash_command = "Let's keep up world!"
    )
    task3 = BashOperator(
        task_id = 'third_task',
        bash_command = "I'll see you again!"
    )

    task1 >> task2 >> task3