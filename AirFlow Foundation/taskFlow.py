from airflow.dacorators import dag, task
from datetime import datetime, timedelta

args ={
    'owner':'task_flow',
    'retries': 3,
    'retry_delay': timedelta(minutes=2)
}

@dag(
    dag_id = 'dag_with_task_flow_v01',
    default_args = args,
    start_date = datetime.now(),
    schedule_interval = None)
def hello_world_etl():
    @task()
    def get_name():
        return "Jinyu"
    
    @task()
    def get_age():
        return 60
    
    @task()
    def greet(name, age):
        print("Hello world, my name is %s, I am %s years old.",name ,age)

    name = get_name
    age = get_age
    greet(name, age)

greet_dag = hello_world_etl()