## Airflow Course Notes

### Instalation on WSL2

Step 1:

sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv
mkdir -p ~/airflow/airflowhome
python3 -m venv ~/airflow/airflowenv
source ~/airflow/airflowenv/bin/activate
pip3 install wheel # Not found in venv by default, but recommended for packages

Step 2:

export AIRFLOW_HOME=~/airflow/airflowhome
AIRFLOW_VERSION=2.3.3
PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
pip3 install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

*execute*:
- airflow standalone
- open in browser http://localhost:8080



### Run airflow with a personal shell script (1. activate venv, 2. export airflowhome path, 3. run airflow standalone command)

- vim run_airflow.sh
source ~/airflow/airflowenv/bin/activate &&
export AIRFLOW_HOME=~/airflow/airflowhome &&
airflow standalone

- chmod 755 run_airflow.sh

- source run_airflow.sh

### Class 14: Definiendo dependencias entre las tareas

tarea1.set_downstream(tarea2)
tarea1 >> tarea2 >> tarea3

en paralelo:

tarea1.set_downstream([tarea1,tarea2])
tarea1 >> [tarea2, tarea3]

### Clase 16: Orquestando un DAG

crontab guru

### Clase 18: Monitoring

Fallos:

1. La API a la que queremos acceder está caída
2. Error de lógica en nuestro código
3. Algún proceso del que dependemos se ejecutó incorrectamente
4. Se ha borrado una tabla de una base de datos
5. Un sensor llegó al timeout

### Clase 21, 22 y 23: Sensores

Los sensores son un tipo especial de operadores que están diseñados para hacer exactamente una cosa: *esperar a que algo ocurre*

*scheduler health and job heartbeat*
- vim airflowhome/airflow.cfg
scheduler_health_check_threshold = 240
job_heartbeat_sec = 20 (default = 5)

### Clase 24: Templates con Jinja


### Clase 25: Xcoms (Cross-communications)
Es un mecanismo que nos permite que las tareas se comuniquien entre sí, pues por defecto estas están totalmente aisladas y pueden estar ejecutándose en máquinas totalmente diferentes.

### Clase 26: BranchPythonOperator
Bifurcación de los pipelines