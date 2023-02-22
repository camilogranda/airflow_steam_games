from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def print_hello():
    print('Hello Universe')


with DAG(dag_id="python_operator",
         description="Our first python operator",
         schedule_interval="@once",
         start_date=datetime(2023, 1, 24)) as dag:
    
    task_1 = PythonOperator(task_id="hello_with_python",
                            python_callable=print_hello)