from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor

with DAG(dag_id="07.3_file_sensor",
         description="File sensor",
         schedule_interval="@daily",
         start_date=datetime(2022,11,1),
         end_date=datetime(2023,2,1)) as dag:

    
    t1 = BashOperator(task_id="file_task",
                      bash_command="sleep 10 && touch /tmp/file.txt")
    
    t2 = FileSensor(task_id="waiting_file",
                    filepath="/tmp/file.txt")
    
    t3 = BashOperator(task_id="end_task",
                      bash_command="echo 'The file has arrived!'")
    
    t1 >> t2 >> t3
    