from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow.utils.trigger_rule import TriggerRule


def my_function():
    raise Exception

# Apply for all tasks
default_args = {}


with DAG(dag_id="06_monitoring_trigger_rules",
         description="Creating dependencies between tasks",
         schedule_interval="@daily",
         start_date=datetime(2022, 11, 1),
         end_date=datetime(2022, 11, 15),
         default_args=default_args,
         max_active_runs=1) as dag:
    
    task_1 = BashOperator(task_id="task_1",
                            bash_command="sleep 2 && echo 'First task!'",
                            retries=2,
                            retry_delay=5,
                            depends_on_past=False,
                            trigger_rule=TriggerRule.ALL_SUCCESS)
    
    task_2 = BashOperator(task_id="task_2",
                            bash_command="sleep 2 && echo 'Second task!'",
                            retries=2,
                            retry_delay=5,
                            trigger_rule=TriggerRule.ALL_SUCCESS)
    
    task_3 = BashOperator(task_id="task_3",
                            bash_command="sleep 2 && echo 'Third task!'",
                            retries=2,
                            retry_delay=5,
                            trigger_rule=TriggerRule.ALWAYS,
                            depends_on_past=False)
    
    task_4 = PythonOperator(task_id="task_4",
                            python_callable=my_function,
                            retries=2,
                            retry_delay=5,
                            trigger_rule=TriggerRule.ALL_SUCCESS)

    task_5 = BashOperator(task_id="task_5",
                            bash_command="sleep 2 && echo 'Fifth task!'",
                            retries=2,
                            retry_delay=5,
                            depends_on_past=True,
                            trigger_rule=TriggerRule.ALL_FAILED)

    task_1 >> task_2 >> task_3 >> task_4 >> task_5