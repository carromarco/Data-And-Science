from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yfin

def download_stock_data():
    hoy = datetime.today().strftime('%Y-%m-%d')
    yfin.pdr_override()
    
    # Lista de empresas
    companies = ['NFLX', 'GOOG', 'AMZN','TSLA','ALUA.BA','MELI','GLOB','KO','YPF','MSFT','TS','SBUX','MCD']
    
    # DataFrame para almacenar todos los datos
    all_data = pd.DataFrame()
    
    for empresa in companies:
        # Obtener los datos de la empresa actual
        data = pdr.get_data_yahoo(empresa, start='2019-01-01', end=hoy)
        
        # Agregar la columna 'Company' con el nombre de la empresa
        data['Company'] = empresa
        
        # Agregar los datos al DataFrame principal
        all_data = pd.concat([all_data, data])
    
    # Si 'Date' no está en el índice, intentamos reindexar para obtenerlo
    if 'Date' not in all_data.columns:
        all_data.reset_index(inplace=True)
    
    # Reorganizar el orden de las columnas
    all_data = all_data[['Date', 'Company', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]
    
    # Guardar el DataFrame como un archivo CSV en tu computadora
    csv_file = 'C:/Users/marco/Desktop/Accesos directos/Desarrollos/No Country/airflow/db/stock_data.csv'  # Cambia esta ruta por la ubicación deseada
    all_data.to_csv(csv_file, index=False)
    
    print(f"Los datos se han guardado en el archivo CSV: {csv_file}")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 2, 22),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'stock_data_pipeline',
    default_args=default_args,
    description='Descargar datos de acciones y guardar en archivo CSV',
    schedule_interval='@daily',
)

task_download_data = PythonOperator(
    task_id='download_stock_data',
    python_callable=download_stock_data,
    dag=dag,
)
