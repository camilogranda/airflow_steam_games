from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(dag_id="07.1_external_dag",
         description="Parent DAG",
         schedule_interval="@daily",
         start_date=datetime(2022,11,1),
         end_date=datetime(2023,2,1)) as dag:
    
    task_external = BashOperator(task_id="external_task_1",
                          bash_command="sleep 10 && echo 'external task executed!'",
                           depends_on_past=True)
    task_external