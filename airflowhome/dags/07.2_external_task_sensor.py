from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
from airflow.sensors.external_task import ExternalTaskSensor

with DAG(dag_id="07.2_external_task_sensor",
         description="Child DAG",
         schedule_interval="@daily",
         start_date=datetime(2022,11,1),
         end_date=datetime(2023,2,1),
         dagrun_timeout=timedelta(minutes=60)) as dag:


     # external_task_id: id de la tarea externa a la que espera por su ejecución
    t1 = ExternalTaskSensor(task_id="waiting_dag",
                                external_dag_id="07.1_external_dag",
                                external_task_id="external_task_1",
                                poke_interval=20)
    
    t2 = BashOperator(task_id="task-2",
                                bash_command="sleep 5 && echo 'DAG 2 ended'",
                                depends_on_past=True)
    
    t1 >> t2