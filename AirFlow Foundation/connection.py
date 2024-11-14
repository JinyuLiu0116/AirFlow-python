from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

args = {
    'owner': 'Postgres',
    'retries': 3,
    'retry_delay': timedelta(minutes = 2)
}


with DAG(
    dag_id = 'dag_with_postgres_operator',
    default_args = args,
    start_date = datetime.now(),
    schedule_interval = None
) as dag:
    task1=PostgresOperator(
        task_id = 'create_postgres_table',
        postgres_conn_id = 'postgres_localhost',
        sql = """
            CREATE TABLE IF NOT EXISTS dag_table(
                dt date,
                dag_id character varying,
                primary key (dt, dag_id)
            )
        """
    )

    task2 = PostgresOperator(
        task_id = 'insert_into_table',
        postgres_conn_id = 'postgres_localhost',
        sql="""
            INSERT INTO dag_table (dt, dag_id value ('{{ ds }}', '{{dag.dag_id}}'))

        """
    )
    task3 = PostgresOperator(
        task_id = 'delete_data_from_table',
        posrgres_conn_id = 'postgres_localhost',
        sql="""
            DELETE FROM dag_table WHERE dt = '{{ ds }}' and dag_id = '{{dag.dag_id}}';
        """
    )
    

    task1 >> task2 >> task3