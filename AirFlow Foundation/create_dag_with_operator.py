from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

args = {
    'owner': 'coder2j',
    'retries': 3,
    'retry_delay' : timedelta(minutes= 2)
}

def greet(ti):
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name', key='last_name' )
    age = ti.xcom_pull(task_ids='get_age', key='age')
    print("Hello World! My name is %s %s,\nand I am %s years old!", first_name, last_name, age)

def get_name(ti):
    ti.xcom_push(key='first_name', value='Jerry')
    ti.xcom_push(key='last_name', value='Fridman')

def get_age(ti):
    ti.xcom_push(key='age', value = 20)

with DAG(
    default_args = args,
    dag_id = 'our_dag_with_python_operator_v01',
    description = 'Our first dag using python operator',
    start_date = datetime(2021, 10, 6),
    schedule_interval = '@daily'
) as dag:
    task1 = PythonOperator(
        task_id = 'greet',
        python_callable = greet,
        
    )
    task2 = PythonOperator(
        task_id = 'get_name',
        python_callable = get_name
    )
    task3 = PythonOperator(
        task_id = 'get_age',
        python_callable = get_age
    )

    [task2, task3] >> task1
    