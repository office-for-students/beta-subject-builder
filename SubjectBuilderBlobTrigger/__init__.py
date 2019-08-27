import logging
import os
import io
import csv

import azure.functions as func

from . import validate, database


def main(subjectblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {subjectblob.name}\n"
                 f"Blob Size: {subjectblob.length} bytes")

    cosmosdb_uri = os.environ["AzureCosmosDbUri"]
    cosmosdb_key = os.environ["AzureCosmosDbKey"]
    throughput = os.environ["DatabaseThroughput"]
    db_id = os.environ["AzureCosmosDbDatabaseId"]
    collection_id = os.environ["AzureCosmosDbSubjectsCollectionId"]
    
    try:
        # Read the Blob into a BytesIO object
        subject_file = io.BytesIO(subjectblob.read())

        csv_bytes = subject_file.read()

        # Decode the bytes into a string
        csv_string = csv_bytes.decode("utf-8-sig")

        rows = csv_string.splitlines()
        number_of_subjects = len(rows) - 1

        # csv header row
        if not validate.column_headers(rows[0]):
            logging.error("file headers are incorrect, expecting the following: code, english_label, level, welsh_label")
            raise exceptions.StopEtlPipelineErrorException

        reader = csv.reader(rows)

        # delete and recreate collection
        database.build_collection(cosmosdb_uri, cosmosdb_key, throughput, db_id, collection_id)

        # add subject docs to new collection
        database.load_collection(cosmosdb_uri, cosmosdb_key, db_id, collection_id, reader)

        logging.info(f"Successfully loaded in {number_of_subjects} subject documents")
        
    except Exception as e:
        # Unexpected exception
        logging.error(
            "SubjectBuilderBlogTrigger unexpected exception ", exc_info=True
        )

        # Raise to Azure
        raise e
