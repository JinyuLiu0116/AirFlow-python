import time
from google.cloud import bigquery

client = bigquery.Client()

dataset_id = 'Staging'
table_id = 'bigquery_copy'

dataset_ref = bigquery.DatasetReference(client.project, dataset_id)
table_ref = bigquery.TableReference(dataset_ref, table_id)
bigquery_table = client.get_table(table_ref)

original_schema = bigquery_table.schema

new_schema = original_schema[:]
new_schema.append(bigquery.SchemaField("saved2", "BOOLEAN", mode="NULLABLE"))
new_schema.append(bigquery.SchemaField("permalink2", "STRING", mode="NULLABLE"))

bigquery_table.schema = new_schema

bigquery_table = client.update_table(bigquery_table, ["schema"])

query_job = client.query("""
    ALTER TABLE `{}.{}`
    DROP COLUMN IF EXISTS saved2,
    DROP COLUMN IF EXISTS permalink2;
""".format(dataset_id, table_id))

while query_job.state != 'DONE':
    print('Waiting for job to finish...')
    time.sleep(3)
    query_job.reload() 

print("Columns deleted successfully.")