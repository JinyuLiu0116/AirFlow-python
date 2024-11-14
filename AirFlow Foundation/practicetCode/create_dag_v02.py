from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

args = {
    'owner': 'saferoom',
    'retries': 3,
    'retry_delay': timedelta(minutes = 2)
}

def getName(ti):
    ti.xcom_push(key = 'first_name', value = 'Jinyu')
    ti.xcon_push(key = 'last_name', value = 'Liu')

def getAge(ti):
    ti.xcon_push(key = 'age', value = 35)

def greed(ti):
    first_name = ti.xcom_pull(task_ids='getName', key = 'first_name')
    last_name = ti.xcom_pull(task_ids = 'getName', key = 'last_name')
    age = ti.xcom_pull(task_ids = 'getAge', key = 'age')
    print("Hello World! My name is %s %s, I am %s years old", first_name, last_name, age)

with DAG(
    default_args = args,
    start_date = datetime.now(),
    schedule_interval = None
) as dag:
    task1 = PythonOperator(
        task_id = 'getName',
        python_callable = getName
    )
    task2 = PythonOperator(
        task_id = 'getAge',
        python_callable = getAge
    )
    task3 = PythonOperator(
        task_id = 'greed',
        python_callable = greed
    )
    [task1, task2] >> task3

    