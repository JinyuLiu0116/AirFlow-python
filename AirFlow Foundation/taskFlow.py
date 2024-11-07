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
    def get_name(multiple_outputs=True):
        return {
            'frist_name': 'Jinyu',
            'last_name': 'Liu'
        }
    
    @task()
    def get_age():
        return 60
    
    @task()
    def greet(first_name, last_name, age):
        print("Hello world, my name is %s %s, I am %s years old.", first_name, last_name, age)

    name = get_name
    age = get_age
    greet(first_name=name['first_name'], last_name=name['last_name'], age=age)

greet_dag = hello_world_etl()