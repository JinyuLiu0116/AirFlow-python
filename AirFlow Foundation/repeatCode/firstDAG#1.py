from airflow import DAG
from datetime import datetime, timedelta #timedelta for retry_delate
from airflow.operators.bash import BashOperator #create task, a task is a implementation of an operator

#common parameters will be used to initialize the 
#operator in default odds
args = {
    'owner': 'jjl',
    'retries': 3,
    'retry_delate': timedelta(minutes=1)
}

def function():
    pass


#use with statement to create an instance of DAG
#all the code will under the slope of the DAG instance
with DAG(
    dag_id = 'my_first_dag_repeat_01',
    default_args = args,
    description = "This is practing in order to be familir with DAGs.",
    start_date = datetime(2024, 10, 27, 8),
    schedule_interval = '@daily'
)as dag:
    task1 = BashOperator(
        task_id = 'first_task',
        bash_command = "Hello world, this is first task!"
    )
    task2 = BashOperator(
        task_id = 'second_task',
        bash_command = "Greating to all, this is second task!"
    )
    task3 = BashOperator(
        task_id = 'third_task',
        bash_command = "Good bye everyone, this is last task!"
    )

    task1 >> task2 >> task3
