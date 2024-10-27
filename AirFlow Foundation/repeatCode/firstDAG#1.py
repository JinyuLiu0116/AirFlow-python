from airflow import DAG
from datetime import datetime, timedelta #timedelta for retry_delate

#common parameters will be used to initialize the 
#operator in default odds
args = {
    'owner': 'jjl',
    'retries': 3,
    'retry_delate': timedelta(minutes=1)
}



#use with statement to create an instance of DAG
#all the code will under the slope of the DAG instance
with DAG(
    dag_id = 'my_first_dag_repeat_01',
    default_args = args,
    description = "This is practing in order to be familir with DAGs.",
    start_date = datetime(2024, 10, 27, 8),
    scheduler_interval = '@daily'
)as dag:
    pass
