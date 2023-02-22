from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime


def print_hello():
    print('Hello Universe')


with DAG(dag_id="dependencies",
         description="Creating dependencies between tasks",
         schedule_interval="@once",
         start_date=datetime(2023, 1, 24)) as dag:
    
    task_1 = PythonOperator(task_id="task_1",
                            python_callable=print_hello)
    
    task_2 = BashOperator(task_id="task_2",
                            bash_command="echo 'tarea_2'")
    
    task_3 = BashOperator(task_id="task_3",
                            bash_command="echo 'tarea_3'")
    
    task_4 = BashOperator(task_id="task_4",
                            bash_command="echo 'tarea_4'")
    
    # task_1.set_downstream(task_2)
    # task_2.set_downstream([task_3, task_4])

    task_1 >> task_2 >> [task_3, task_4]

