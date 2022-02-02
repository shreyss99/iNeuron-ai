from data_access_layer.mongo_db.mongo_db_atlas import MongoDBOperation
from project_library_layer.credentials.credential_data import get_aws_credentials
import pandas as pd
from cloud_storage_layer.aws.amazon_simple_storage_service import SimpleStorageService



if __name__=="__main__":
    s=SimpleStorageService()
    s.create_bucket("avnish-327030")

