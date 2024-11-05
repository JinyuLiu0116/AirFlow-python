from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

args = {
    'owner': 'coder2j',
    'retries': 3,
    'retry_delay' : timedelta(minutes= 2)
}

def greet(name, age):
    print("Hello World! My name is %s,\nand I am %s years old!", name, age)




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
        op_kwargs = {'name': 'Tom', 'age': 20}
    )

    task1
   