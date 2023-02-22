from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# ds: logical date
templated_command = """ 
{% for file in params.filenames %}
    echo "{{ ds }}"
    echo "{{ file }}"
{% endfor %}
"""

with DAG(dag_id="08_templating",
         description="Example using templates",
         schedule_interval="@daily",
         start_date=datetime(2022,12,1),
         end_date=datetime(2023,1,1)) as dag:
    
    task_1 = BashOperator(task_id="task_1",
                           bash_command=templated_command,
                           params={"filenames": ["file1.txt","file2.txt"]},
                           depends_on_past=True)
    task_1