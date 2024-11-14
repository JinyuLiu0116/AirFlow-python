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

    