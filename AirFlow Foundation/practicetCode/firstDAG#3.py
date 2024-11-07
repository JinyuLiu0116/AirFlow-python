from airflow import DAG
from airflow.operators.bash import BashOperater
from datetime import datetime, timedelta

args = {
    'onwer' : 'itRoom',
    'retries' : 3,
    'retry_delay' : timedelta(minutes = 2)
}

with DAG(
    dag_id = 'repeat_dag_untill_bum',
    default_args = args,
    description = "pacticing will make different",
    start_date = datetime(2024, 10, 30, 4),
    schedule_interal = '@daliy'

) as dag:
    task1 = BashOperater(
        task_id = 'first_task',
        bash_command = "MY first task"
    )
    task2 = BashOperater(
        task_id = 'second_task',
        bash_command = "My second task"
    )
    task3 = BashOperater(
        task_id = 'third_task',
        bash_command = "My third task"
    )
    task4 = BashOperater(
        task_id = 'fourth_task',
        bash_command = "work with my third task"
    )

    task1 >> task2 >> [task3/task4]
