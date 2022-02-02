from cloud_storage_layer.google.google_cloud_storage import GoogleCloudStorage
from data_access_layer.mongo_db.mongo_db_atlas import MongoDBOperation
import time
import os,sys
from google.cloud import storage
from google.oauth2 import service_account
import pandas as pd
from sklearn.linear_model import LinearRegression
from cloud_storage_layer.google.google_cloud_storage import GoogleCloudStorage
try:

    gcp=GoogleCloudStorage()
    print(gcp.list_files('company_name/report/graph/project/Mushroom_Classifier/Graph_2021_04_01_18_28_01/'))
    #df=gcp.read_file_content("company_name/prediction/data/project/Thyroid_Detection/prediction_output_file","Output.csv")
   # print(df)
    #gcp.create_directory("company_name/prediction/data/project/Wafer Fault detection/prediction_batch_files")
    """
    print(gcp.list_directory('company_name/training/data/project/Wafer Fault detection/good_raw_data_files'))
    df=pd.DataFrame({'id':[1,23,]})
    df.reset_index(drop=True,inplace=True)
    #gcp.write_file_content('testing','test.csv',df)
    df1=gcp.read_file_content('company_name/training/data/project/Wafer Fault detection/training_file_from_db/','InputFile.csv')
    df1=df1['file_content']
    print("Hi")
    #df=gcp.read_file_content('company_name/training/data/project/Wafer Fault detection/good_raw_data_files','wafer_13012020_090817.csv')['file_content']

    print(df)
    #gcp.create_directory("company_name/training/data/project/Wafer Fault detection/training_batch_files")
    #print(gcp.create_bucket("avnish-327030"))
    #print(gcp.list_buckets())
    #print([b.name for b in gcp.client.list_blobs(bucket_or_name="machine-learning-327030")])
    #print(gcp.list_directory("company name/"))
    #print#blob=gcp.bucket.blob('testing/yadav/ashish/').upload_from_string("")(gcp.is_directory_present("company name/","kubeflow-test-910e25a1b7c4.json"))
    #gcp.create_directory("data/project/project_name")
    #print(gcp.remove_file("company name/",'kubeflow-test-910e25a1b7c4.json'))
    #response=gcp.download_file("data","input_file.csv",local_system_directory=False)
    #with open('trail.csv','wb') as f:
    #    f.write(response['file_object'].getvalue())
    """


    #lr=LinearRegression()
    #print(gcp.write_file_content('model','Linear.sav',lr))
    #print(gcp.read_file_content('model','Linear.sav'))
    #print(gcp.move_file('model','machine_model','Linear.sav',over_write=True))
except Exception as e:
    print(e)
    exc_type, exc_obj, exc_tb = sys.exc_info()
    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_tb.tb_lineno,file_name)