import time
from google.cloud import bigquery

client = bigquery.Client()

dataset_id = 'Staging'
table_id = 'bigquery_copy'

dataset_ref = bigquery.DatasetReference(client.project, dataset_id)
table_ref = bigquery.TableReference(dataset_ref, table_id)
bigquery_table = client.get_table(table_ref)

original_schema = bigquery_table.schema