from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(dag_id="bash_operator",
         description="Using bash operator",
         start_date=datetime(2023,1,12)) as dag:
    
    task_1 = BashOperator(task_id="hello_with_bash",
                           bash_command="echo 'Hello Universe'")
    task_1