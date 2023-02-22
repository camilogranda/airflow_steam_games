from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime


with DAG(dag_id="orchestration",
         description="Testing Orchestration ",
         schedule_interval="@daily",
         start_date=datetime(2023, 1, 2),
         end_date=datetime(2023, 1, 18),
         default_args={"depends_on_past":True},
         max_active_runs=1) as dag:
    
    # task_1 = BashOperator(task_id="task_1",
    #                      bash_command="sleep 2 && echo 'Task_1'")
                            
    task_2 = BashOperator(task_id="task_2",
                         bash_command="sleep 1 && echo 'Task_2'")
                            
    task_3 = BashOperator(task_id="task_3",
                         bash_command="sleep 1 && echo 'Task_3'")
                            
    task_4 = BashOperator(task_id="task_4",
                         bash_command="sleep 1 && echo 'Task_4'")
    
    task_5 = BashOperator(task_id="task_5",
                          bash_command="sleep 1 && echo 'Task_5'")
                        
    task_2 >> [task_3, task_4] >> task_5