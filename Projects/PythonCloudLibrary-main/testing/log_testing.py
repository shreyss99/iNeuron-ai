from logging_layer.logger.log_request import LogRequest
from data_access_layer.mongo_db.mongo_db_atlas import MongoDBOperation
import uuid
from datetime import datetime
from dateutil.parser import parse
from project_library_layer.datetime_libray.date_time import get_difference_in_second,get_difference_in_milisecond
import os,sys
try:
    m=MongoDBOperation()
    response=m.get_record('Fail_log','request',query={'executed_by':"yadav.tara.avnish@gmail.com"})
    diff=get_difference_in_second(response['log_stop_date'] + " " +response['log_stop_time'],
                                  response['log_start_date'] + " " +response['log_start_time'],)
    print(diff)
    diff=get_difference_in_milisecond(response['log_stop_date'] + " " +response['log_stop_time'],
                                  response['log_start_date'] + " " +response['log_start_time'],)
    print(diff)
    """
    executed_by='yadav.tara.avnish@gmail.com'
    execution_id=uuid.uuid4().__str__()
    app_log=LogRequest('Fail_log','request',executed_by,execution_id)
    app_log.log_start()
    response={'status':True,'message':'Testing message'}
    app_log.log_stop(response)
    """

except Exception as e:
    #log_excep=LogExceptionDetail(execution_id=execution_id,executed_by=executed_by)
    #log_excep.log(None,str(e))
    print(e)
    exc_type, exc_obj, exc_tb = sys.exc_info()
    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_tb.tb_lineno, file_name)