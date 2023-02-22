from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime


def my_function():
    pass


with DAG(dag_id="06_monitoring",
         description="Creating dependencies between tasks",
         schedule_interval="@daily",
         start_date=datetime(2022, 11, 1),
         end_date=datetime(2022, 11, 15)) as dag:
    
    task_1 = BashOperator(task_id="task_1",
                            bash_command="sleep 2 && echo 'First task!'")
    
    task_2 = BashOperator(task_id="task_2",
                            bash_command="sleep 2 && echo 'Second task!")
    
    task_3 = BashOperator(task_id="task_3",
                            bash_command="sleep 2 && echo 'Third task!'")
    
    task_4 = PythonOperator(task_id="task_4",
                            python_callable=my_function)

    task_5 = BashOperator(task_id="task_5",
                            bash_command="sleep 2 && echo 'Fifth task!'")

    task_1 >> task_2 >> task_3 >> task_4 >> task_5