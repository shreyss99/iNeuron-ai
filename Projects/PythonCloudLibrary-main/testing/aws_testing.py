from cloud_storage_layer.aws.amazon_simple_storage_service import AmazonSimpleStorageService
import os,sys
import pandas as pd
from sklearn.linear_model import LinearRegression
from data_access_layer.mongo_db.mongo_db_atlas import MongoDBOperation
import uuid
from project_library_layer.initializer.initializer import Initializer
try:
    i=Initializer()
    print(i.get_session_secret_key())
    #root_dir="mega_challenge"
    #m=MongoDBOperation()
    #m.insertRecordInCollection("session","secretKey",{'secret-key':str(uuid.uuid4())})
    #print()
    #s3=AmazonSimpleStorageService()
    """
    
    data=root_dir+"/data"
    default_training=data+"/default_training"
    projects=default_training+"/projects"
    project_name=projects+"/wafer_fault_detection"
    s3.create_directory(project_name)
    
    print(s3.remove_directory("mega_challenge/data"))
    
    print(s3.create_directory("machine_learning/data/default_training/projects",over_write=True))
    print(s3.create_directory("machine_learning/data/default_training/", over_write=True))
    print(s3.create_directory("machine_learning/prediction_files/", over_write=False))
    print(s3.create_directory("machine_learnings/prediction_files/", over_write=False))
    
    print(s3.upload_file("machine_learning/", "app.txt","D:/number.txt"))
    print(s3.list_files('machine_learning//'))

    print(s3.remove_directory(""))#)machine_learning/data/default_training/projects"))
    print(s3.list_files("machinelearning/data/default_training/projects/"))
    print(s3.is_file_present("machinelearning/data/default_training/projects/","PCA.txt"))
    df=pd.DataFrame({'name':['avnish']})
    lr=LinearRegression()
    print(s3.write_file_content("avn/manish","linaer.sav",lr))
    """
    print(s3.list_directory("Resume"))
    #print(s3.list_directory("avn/"))
    #print(s3.move_file("avn/manish/","avn/manish/yadav","InputFile.csv",over_write=True))
    #print(s3.list_directory("mega_challenge/data/default_training/projects/wafer_fault_detection"))
except Exception as e:
    print(e)
    exc_type, exc_obj, exc_tb = sys.exc_info()
    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_tb.tb_lineno,file_name)