from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

# 1. Context manager
with DAG(dag_id="first_dag",
         description="Our first DAG",
         start_date=datetime(2022,7,1),
         schedule_interval="@once"
         ) as dag:
    t1 = EmptyOperator(task_id="dummy")
    t1

# 2. Creating DAG instance
dag_2 = DAG(dag_id="second_dag",
         description="Our first DAG",
         start_date=datetime(2022,8,23),
         schedule_interval="@once")

operator_2 = EmptyOperator(task_id="dummy_2", dag=dag_2)

# Using DAG decorator
# @dag(
#      dag_id="third_dag",
#      description="Our third DAG",
#      start_date=datetime(2022,9,25),
#      schedule_interval="@once"
#      )
# def generate_dag():
#     operator_3 = EmptyOperator(task_id="dummy_3")

