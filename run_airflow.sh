#!/bin/bash

source ./airflowhome/airflowenv/bin/activate &&
export AIRFLOW_HOME=~/13-airflow/airflowhome && 
airflow standalone 
