from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from datetime import datetime, timedelta

args={
    'owner': 'airflow',
    'retries': 3,
    'retry_delay': timedelta(minutes=2)
}

def get_name(ti):
    ti.xcom_push(key='first_name', value='Tom')
    ti.xcon_push(key='last_name', value='Strom')

def get_age(ti):
    ti.xcom_push(key='age', value=22)

def greet(ti):
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name', key='last_name')
    age = ti.xcom_pull(task_ids='get_age', key='age')
    print("Hello world, my name is %s %a, I am %s years old", first_name, last_name, age)

with DAG(
    default_args = args,
    dag_id = 'hellow_world_v01',
    start_date = datetime.now(),
    schedule_interval = None
) as dag:
    start = DummyOperator(task_id = 'satrt')

    task1 = PythonOperator(
        task_id = 'greet',
        python_callable= greet,
        dag=dag
    )
    task2 = PythonOperator(
        task_id = 'get_name',
        python_callable = get_name,
        dag=dag
    )
    task3 = PythonOperator(
        task_id ='get_age',
        python_callable=get_age,
        dag=dag
    )

    end = DummyOperator(task_id ='end')

    start >> [task2, task3] >> task1 >> end
