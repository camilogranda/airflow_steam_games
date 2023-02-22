from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.operators.email import EmailOperator
from datetime import datetime
import steam_new_releases as scraper
import time
import json
import pandas as pd


date = time.strftime("%Y-%m-%d")

def fetch_games(ti):
    """ 
    Fetch new releases from Steam Store
    """
    games = scraper.steam_new_releases()
    print(games[0])
    ti.xcom_push(key="games_list", value=games)
    
def save_as_files(ti):
    """ 
    Save steam games as JSON and CSV files
    """
    games = ti.xcom_pull(key="games_list", task_ids="fetch_games")
        
    with open(f'/home/milo/13-airflow/airflowhome/files/new_games_{date}.json', mode='w', encoding='utf-8') as f:
        json.dump(games, f, ensure_ascii=False)
    print('Saved as .JSON!')
        
    games_df = pd.DataFrame(games)
    games_df.to_csv(f'/home/milo/13-airflow/airflowhome/files/new_games_{date}.csv', index=False)
    print('Saved as .csv!')
    
    print('Today New Games:')
    for game in games:
        print(game['game'] + ' ' + '[' + game['tags'] + ']')
    print('')
    print('Visit the official Steam Store to see more: https://store.steampowered.com/explore/new/')
        

with DAG(dag_id="steam_dag",
         description="steam new releases",
         start_date=datetime(2022,7,1),
         end_date=datetime(2022,7,2),
         schedule_interval="@once"
         ) as dag:

    fetch_games = PythonOperator(task_id="fetch_games",
                           python_callable=fetch_games)
    
    message_1 = BashOperator(task_id="games_list",
                           bash_command="echo 'Games Fetched!'")
    
    save_files = PythonOperator(task_id="save_data",
                                python_callable=save_as_files)
    
    message_2 = BashOperator(task_id="files_saved",
                           bash_command="echo 'File saved as .csv and .JSON!'")
