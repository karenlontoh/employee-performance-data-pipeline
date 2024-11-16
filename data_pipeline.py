'''
Preface

This program is designed to automate the process of fetching raw data from a PostgreSQL database, cleaning the data, and then posting it to Elasticsearch for further analysis. It uses Apache Airflow to manage the workflow, ensuring tasks run in sequence and at scheduled intervals. The steps include extracting data, cleaning it by handling missing values and duplicates, and then indexing the cleaned data into Elasticsearch for easy access and querying.
'''

# Import Libraries
import pandas as pd
import psycopg2 as db
import datetime as dt
from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

# Fetch data from PostgreSQL
def fetch_from_postgresql():
    '''
    This function is used to fetch data from PostgreSQL and save it as a CSV file.

    The function connects to a PostgreSQL database using a predefined connection string, executes a query to fetch data 
    from a specific table, and then saves the result in CSV format to a specified location.

    No parameters are required as the connection string and query are already defined within the function.

    Return:
        None - This function does not return any value; it performs the data fetching and saving process.

    Example usage:
        In an Airflow DAG, this function is called as part of the workflow:
        fetch_data = PythonOperator(
            task_id='fetch_from_postgresql', 
            python_callable=fetch_from_postgresql
        )

    Notes:
        This function fetches data from the `employee_performance` table in the PostgreSQL database and saves it as a CSV file 
        named 'raw_data.csv' in the `/opt/airflow/dags/` directory.
    '''
    conn_string = "dbname='postgres' host='postgres' user='airflow' password='airflow'"
    conn = db.connect(conn_string)
    query = "SELECT * FROM employee_performance;"
    
    # Fetch data from PostgreSQL
    df = pd.read_sql(query, conn)
    conn.close()

    # Save the raw data to a CSV file
    df.to_csv('/opt/airflow/dags/raw_data.csv', index=False)
    print("Data fetched from PostgreSQL and saved to CSV.")

# Data Cleaning
def data_cleaning():
    '''
    This function performs data cleaning operations on a raw dataset.

    The function reads the raw dataset from a CSV file, then applies several data cleaning steps:
    1. Removes duplicate rows.
    2. Handles missing values:
       - For numeric columns (float and int), missing values are replaced with the median of the column.
       - For non-numeric columns, missing values are replaced with 'Unknown'.
    3. Normalizes column names by stripping spaces and converting them to lowercase.
    
    After cleaning, the function saves the cleaned data to a new CSV file.

    Return:
        None - This function does not return any value; it performs data cleaning and saves the cleaned data to a new CSV file.

    Example usage:
        In an Airflow DAG, this function is called as part of the workflow:
        clean_data = PythonOperator(
            task_id='data_cleaning', 
            python_callable=data_cleaning
        )

    Notes:
        The cleaned dataset is saved to the file '/opt/airflow/dags/clean_data.csv'.
    '''
    df = pd.read_csv('/opt/airflow/dags/raw_data.csv')

    # 1. Remove duplicates
    df = df.drop_duplicates()

    # 2. Handle missing values
    for column in df.columns:
        if df[column].dtype == 'float64' or df[column].dtype == 'int64':
            df[column].fillna(df[column].median(), inplace=True)
        else:
            df[column].fillna('Unknown', inplace=True)

    # 3. Normalize column names
    df.columns = df.columns.str.strip()  # Remove leading/trailing spaces/tabs from column names
    df.columns = df.columns.str.lower()  # Convert all column names to lowercase

    # Save the cleaned data to a CSV file
    df.to_csv('/opt/airflow/dags/clean_data.csv', index=False)
    print("Data cleaned and saved to CSV.")

# Post cleaned data to ElasticSearch
def post_to_elasticsearch():
    '''
    This function posts cleaned data to an Elasticsearch index.

    The function connects to an Elasticsearch instance, reads a cleaned dataset from a CSV file,
    and indexes the data into an Elasticsearch index called 'milestone3_karen'. It uses bulk indexing 
    to efficiently upload multiple records at once.

    The cleaned dataset is expected to be in CSV format, where each row is indexed as a separate document 
    in Elasticsearch.

    Return:
        None - This function does not return any value; it performs data indexing to Elasticsearch.

    Example usage:
        In an Airflow DAG, this function is called as part of the workflow:
        post_to_elastic = PythonOperator(
            task_id='post_to_elasticsearch', 
            python_callable=post_to_elasticsearch
        )

    Notes:
        The Elasticsearch instance is accessed through the host 'elasticsearch' at port 9200.
        The function uses the `bulk` helper function from the `elasticsearch.helpers` module for efficient indexing.
        The data is indexed into the 'milestone3_karen' index in Elasticsearch.
    '''
    es = Elasticsearch([{'host':'elasticsearch', 'port':9200,'scheme':'http'}])
    df = pd.read_csv('/opt/airflow/dags/clean_data.csv')

    actions = [
        {
            "_index": "employee_data",  
            "_source": r.to_dict()   
        }
        for _, r in df.iterrows() 
    ]

    # Bulk indexing
    bulk(es, actions)
    print(f"Successfully indexed {len(actions)} documents to Elasticsearch.")

# DAG configuration
default_args = {
    'owner': 'karen',
    'start_date': dt.datetime(2024, 11, 8) - timedelta(minutes=10)
}

with DAG('m3_karen',
         description='raw data from PostgreSQL to cleaned data and post to Elasticsearch',
         default_args=default_args,
         schedule_interval='30 6 * * *',
         catchup=False
         ) as dag:
    
    # Ensure proper indentation of task definitions
    fetch_data = PythonOperator(
        task_id='fetch_from_postgresql', 
        python_callable=fetch_from_postgresql
    )

    clean_data = PythonOperator(
        task_id='data_cleaning', 
        python_callable=data_cleaning
    )

    post_to_elastic = PythonOperator(
        task_id='post_to_elasticsearch', 
        python_callable=post_to_elasticsearch
    )

    # Task dependencies
    fetch_data >> clean_data >> post_to_elastic