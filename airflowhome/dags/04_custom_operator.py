from airflow import DAG
from hellooperator import HelloOperator
from datetime import datetime


with DAG(dag_id="custom_operator",
         description="Our first custom operator",
         schedule_interval="@once",
         start_date=datetime(2023, 1, 24)) as dag:
    
    task_1 = HelloOperator(task_id="hello",
                           name="milo")
    
    task_1