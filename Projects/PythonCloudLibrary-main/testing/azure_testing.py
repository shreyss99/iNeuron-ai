from cloud_storage_layer.microsoft_azure.azure_blob_storage import MicrosoftAzureBlobStorage
import time
import os,sys
import pandas as pd
from sklearn.linear_model import LinearRegression
from integration_layer.file_management.file_manager import FileManager
try:
    mzb=MicrosoftAzureBlobStorage()

    mzb=FileManager('microsoft')
    print(mzb.list_files("company_name/report/graph/project/BigMart_Sales/414372f0-2a99-4142-a688-faeda7a65bce"))
    """
    print(mzb.list_files("avnas"))
    print(mzb.create_directory("company_name/data/projects/project_name"))
    print(mzb.remove_directory(""))

    print(mzb.upload_file("avn/manish/ashish", "number.txt",r"D:\number.txt"))

    print(mzb.remove_file("avn/manish/ashish","number.txt"))
    print(mzb.write_file_content('model','linear.sav',LinearRegression(),over_write=True))
    print(mzb.read_csv_file("","wafer_07012020_041011 (1).csv"))
    print(mzb.read_file_content('model','linear.sav'))
    print(mzb.read_file_content('model', 'linear.sav')['file_content'])
    print(mzb.move_file('model','modelasbha','linear.sav',over_write=True))
    """

except Exception as e:
    print(e)
    exc_type, exc_obj, exc_tb = sys.exc_info()
    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_tb.tb_lineno,file_name)