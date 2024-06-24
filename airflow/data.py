from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import psycopg2

# Función para extraer datos financieros de la base de datos en línea
def extract_financial_data():
    # Conectar a la base de datos
    conn = psycopg2.connect(
        dbname="airflow",
        user="airflow",
        password="airflow",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    
    # Ejecutar consulta SQL para extraer datos financieros
    cursor.execute("SELECT * FROM tabla_datos_financieros;")
    data = cursor.fetchall()
    
    # Procesar los datos (por ejemplo, guardarlos en un archivo CSV)
    with open("financial_data.csv", "w") as f:
        for row in data:
            f.write(",".join(map(str, row)) + "\n")
    
    # Cerrar la conexión
    cursor.close()
    conn.close()

# Definir los argumentos de la DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 2, 15),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1
}

# Definir la DAG
dag = DAG(
    'extract_financial_data',
    default_args=default_args,
    description='Pipeline para extraer datos financieros',
    schedule_interval='0 0 * * *',  # Ejecutar diariamente a la medianoche
)

# Definir el operador Python
extract_data_task = PythonOperator(
    task_id='extract_financial_data_task',
    python_callable=extract_financial_data,
    dag=dag,
)

# Definir la secuencia de tareas
extract_data_task
