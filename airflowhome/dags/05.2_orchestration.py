from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime


with DAG(dag_id="orchestration_2",
         description="Testing Orchestration again",
         schedule_interval="0 7 * * 1",
         start_date=datetime(2023, 1, 2),
         end_date=datetime(2023, 2, 2)) as dag:
    
    task_1 = EmptyOperator(task_id="task_1")
                            
    task_2 = EmptyOperator(task_id="task_2")
                            
    task_3 = EmptyOperator(task_id="task_3")
                            
    task_4 = EmptyOperator(task_id="task_4")
                            
    task_1 >> task_2 >> task_3 >> task_4

