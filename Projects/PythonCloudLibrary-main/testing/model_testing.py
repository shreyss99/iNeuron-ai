from project_library_layer.initializer.initializer import Initializer
from cloud_storage_layer.microsoft_azure.azure_blob_storage import MicrosoftAzureBlobStorage
from controller.project_controller.projects.WaferFaultDetection_new.file_operations import file_methods
from logging_layer.logger.logger import AppLogger
import uuid

log_writer = AppLogger(project_id=10, executed_by='yadav.tara.avnish@gmail.com',
                                        execution_id=str(uuid.uuid4()), socket_io=None)
file_object=MicrosoftAzureBlobStorage()
file_loader = file_methods.FileOperation(project_id=10, file_object=file_object,
                                                     logger_object=log_writer)

model_name = file_loader.find_correct_model_file(str(0))
model = file_loader.load_model(model_name)
print(model.get_booster().feature_names)
model_name = file_loader.find_correct_model_file(str(1))
model = file_loader.load_model(model_name)
print(model.get_booster().feature_names)
model_name = file_loader.find_correct_model_file(str(2))
model = file_loader.load_model(model_name)
print(model.get_booster().feature_names)

"""
prediction failed due to :Failed during prediction 
from in module [entity_layer.predict_from_model.prediction_from_model] 
class [ProjectConfiguration] method [prediction_from_model]
python script name [prediction_from_model.py] line number [89] error message
[Failed during prediction in module [controller.project_controller.projects.bigmart_sales.prediction_model_bigmart_sales] 
class [Prediction] method [prediction_from_model] python script name [prediction_model_bigmart_sales.py] line number
[86] error message [feature_names mismatch:
['Item_Weight', 'Item_Visibility', 'Item_MRP', 'Outlet_Years', 'Item_Fat_Content_0', 'Item_Fat_Content_1',
 'Outlet_Location_Type_0', 'Outlet_Location_Type_1', 'Outlet_Location_Type_2', 'Outlet_Size_0', 'Outlet_Size_1',
 'Outlet_Size_2', 'Outlet_Size_3', 'Outlet_Type_0', 'Outlet_Type_1', 'Outlet_Type_2', 'Outlet_Type_3',
 'Item_Type_Combined_0', 'Item_Type_Combined_1', 'Item_Type_Combined_2', 'Outlet_0', 'Outlet_1', 
 'Outlet_2', 'Outlet_3', 'Outlet_4', 'Outlet_5', 'Outlet_6', 'Outlet_7', 'Outlet_8', 'Outlet_9']
    
['f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12',
 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f20', 'f21', 'f22', 'f23', 
 'f24', 'f25', 'f26', 'f27', 'f28', 'f29'] 

expected 
Item_Fat_Content_0, Outlet_Type_3, Outlet_9, Outlet_0, Outlet_1,
Outlet_Location_Type_0, Item_Type_Combined_0,
Outlet_6, Outlet_Type_1, Outlet_Location_Type_2, 
Outlet_2, Outlet_Years, Item_MRP, Item_Visibility,
Outlet_Size_0, Outlet_3, Outlet_Location_Type_1, Outlet_Size_1,
Item_Weight, Outlet_Type_2, Outlet_8, Outlet_Type_0, 
Outlet_Size_3, Outlet_5, Item_Fat_Content_1, Item_Type_Combined_1,
Outlet_Size_2, Outlet_7, Outlet_4, Item_Type_Combined_2 in 

input data training data did not have the following fields:
f21, f10, f8, f19, f7, f18, f26, f17, f29, f20, f25, f4, f3, f16, f1, f9, f11, f28, f2, f14, f24, f23, f27, f5, f15, f13, f12, f0, f6, f22]]

"""