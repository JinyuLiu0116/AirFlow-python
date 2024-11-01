import time
from google.cloud import bigquery

client = bigquery.Client()

dataset_id = 'Staging'
table_id = 'bigquery_copy'

dataset_ref = client.dataset(dataset_id)
table_ref = dataset_ref.table(table_id)

bigquery_table = client.get_table(table_ref)