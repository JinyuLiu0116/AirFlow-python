import time
from google.cloud import bigquery

client = bigquery.Client()

dataset_ref = bigquery.DatasetReference(client.project, 'Staging')#'dataset id'
table_ref = bigquery.TableReference(dataset_ref, 'bigquery_copy')#'table name'
bigquery_table = client.get_table(table_ref)

#get a snapshot of the table schema
original_schema = bigquery_table.schema # schema atribut provids a list

# add colums
new_schema = original_schema[:] #creates a copy of the schema

new_schema.append(bigquery.SchemaField("saved2", "BOOLEAN", mode="NULLABLE"))
new_schema.append(bigquery.SchemaField("permalink2", "STRING", mode="NULLABLE"))

# assign the updated schema to the bigquery_table
bigquery_table.schema = new_schema

#make an API requerst to add columns 
client.update_table(bigquery_table, ['schema'])

#delete columns
query_job = client.query("""
    ALTER TABLE Staging.bigquery_copy
    DROP COLUMN IF EXISTS saved2,
    DROP COLUMN IF EXISTS permalink2;
""")

while query_job.state != 'DONE':
    print('Waiting for job to finish...')
    time.sleep(3)
    query_job.reload()
print(query_job.result())