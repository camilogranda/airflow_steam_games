from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime


default_args = {"depends_on_past":True}

# ti: task instance
def myfunction(**context):
    print(int(context["ti"].xcom_pull(task_ids="task_2_pull")) -6)

with DAG(dag_id="09_Xcoms",
         description="Example using templates",
         schedule_interval="@daily",
         default_args=default_args,
         start_date=datetime(2023,1,1),
         max_active_runs=1) as dag:
    
    # La tarea 2 obtiene el resultado de la tarea 1 por medio de las xcom
    
    task_1 = BashOperator(task_id="task_1_source",
                          bash_command="sleep 5 && echo $((5 * 3))")
    
    task_2 = BashOperator(task_id="task_2_pull",
                          bash_command="sleep 3 && echo {{ ti.xcom_pull(task_ids='task_1_source') }}")
    
    task_3 = PythonOperator(task_id="task_3_pull",
                            python_callable=myfunction)
    
    task_1 >> task_2 >> task_3