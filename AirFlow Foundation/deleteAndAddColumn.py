import time
from google.cloud import bigquery

client = bigquery.Client()

dataset_ref = bigquery.DatasetReference(client.project, 'Staging')
table_ref = bigquery.TableReference(dataset_ref, 'bigquery_copy')
bigquery_table = client.get_table(table_ref)
