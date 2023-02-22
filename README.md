# airflow_steam_games
Data pipeline with airflow that fetch steam new realeases and save them as .JSON and .csv files. Also, a log with all the games and tags are printed.

HOW TO RUN:

1. Activate virtual environment and launch Airflow webserver exexuting the file *run_airflow.sh*:
  **source run_airflow.sh**
  
2. Open in Browser http://localhost:8080

3. On Airflow Webserver, run "steam_dag.py" DAG

4. See in the logs of the task number three (save_files) the latests releases of Steam Store
