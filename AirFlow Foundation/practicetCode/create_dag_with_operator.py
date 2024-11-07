from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

args = {
    'owner' : 'practice',
    'retries' : 3,
    'retry_delay' : timedelta(minutes=2)
}
def get_name(ti):
    ti.xcom_push('first_name', value='Jinyu')
    ti.xcom_push('last_name', value='Liu')

def get_age(ti):
    ti.xcom_push('age', value=60)

def greet(ti):
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name = ti.xcom_pull(task_ides='get_name', key='last_name')
    age = ti.xcom_pull(task_ids='get_age', key='age')

    print("Hello world, my name is %s %s, I am %s years old", first_name, last_name, age)


with DAG(
    default_args = args,
    dag_id = 'our_dag_with_python_operator_v02',
    start_date = datetime.now(),
    schedule_interal = None
) as dag:
    task1 = PythonOperator(
        task_id = 'get_name',
        python_callable=get_name
    )
    task2 = PythonOperator(
        task_id = 'get_age',
        python_callable = get_age
    )
    task3 = PythonOperator(
        task_id='greet',
        python_callable=greet
    )
    [task1, task2] >> task3
    