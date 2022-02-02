try:
    from data_access_layer.mongo_db.mongo_db_atlas import MongoDBOperation
    import sys,os
    import pandas as pd
    #data={
    """
  "type": "service_account",
  "project_id": "kubeflow-test-306307",
  "private_key_id": "910e25a1b7c4dd78276faf85013f1f2aab7683f3",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCg7v3WdDO4Zpy9\nYtZkdkGHCSl85VSEYHF02ARQYRo1AgCWnFRNzFQiOqWCl1ztmTejEhvHYlAcVyIp\noow3pIq5eb2l2VsALTmoVXNz6xGf6RS60bsgEzxQoRizz6g2P/oqQO/f/uVgzGkr\ncBE8/5zTlSmIqJ/+MVFHVJhSNWGknbxJTS3uA4Ycl2M1GCsJLFLo2ezUbDCPSEk1\nbB99O09wUakSlhEG6bct5b5gN8RUS5NPiB5q6V8mqcK2DP+eiJ651pOV2MTx7JLR\na33ijmCmE1fp73GnvsCNDZUx/H+oKQRcGbTvsYM2OUDzia6ZnklkG8rrKKpKoPkj\ncrNw2MX5AgMBAAECggEAA92NrQacPeoACof61o2lGAdbLt/qwmW3H+t22g/lA2At\nj7CIUViOrkZKlqsITUAsfw8Wqfi1bCLXJBkehVEfUGJpUNgaSJQtgfqwc9ix8w10\nBSM3u4bewGCIMXxzwb7SZUyrPk326DbssUGHNnf8xjO7XEgRlLdOSJhycqoL0vp5\npLpy2sLxoNxCZUJe4fjw6PtHAxdxxTvoojjxTsxHd3j7ybHuGaMzrPk7T0qQveP8\nLzqmrmd+BoqiGdaVUjxZUx1VWDobPX4N5WzRgKcMrNJQyH/2d1oaycWiqJ7bmOFF\n2FhIsjFrg4STWhNf57dGfMb5hA5231Wf0PIIYztzIQKBgQDb6SzDWJXbljVtE4nS\nx7jw4m1Vhg/diMt4AQyoB0aaW0XpXLSj0zbNXv7iAd34wKCCoU7tYa1tCoxXoSSb\nDXRy34Di0B0u9Ry2j3SoJt5ao8x+B7L4HvA1qfYCEvGs5Koxv+KUrLqBg02QbKwZ\ncMM/nApDvG7KVgT5+5JGnOdKYQKBgQC7WBTv/MrPX0SgR5vcUQKzDDphSyfg1H2H\np3ZAEQJtR+A5KoMIZqeUdbwQOTXJoebxA6GDUV9957jjxzOfu4SUWT3kZcn75lyd\nTYl6XDHpXccrZDLYLK+J6Tk1sHi0mQeJoZTa8buNU6+uEBFxxdh2y8t32X2m/ISN\nsI0Vg3KSmQKBgQCjlcW9nrUDPq6JcEJS8Ezrq5OnTe2ZXvv0TduLVrY3dnQADv00\n7JZUmTjDCJ6FP01nPvVGciWe+nzBZtajHJQmK4plrmg3GRB94SLnPtqi1Dv2+GUy\nW1lWohKlIlByyzqrfVDgRckLNJBLQfuXhSFIvRuJna9QhkJ3bqM2Mdt/oQKBgQCw\nVqVGi0R+0uZuk1iilOIclBrzb2F236vUnwzQGvKU2D22sUwrAS0lsXg2MRNu2eTd\n4RQK3fIrOYyvYdY2uLN/S0zVifYIE/oC2nPX56XXSjzpm+O71LvZ7Nu7rILBQvV0\nV9IcD8MAsM/A4ED7PUWV9BdtlRsPrco67/6sTFDwqQKBgDo2rEjsC8uJRcOkUk64\nijvLDM+CmDOao1W2oEYP8gfb4mbYs254OzHVSh0fLzsAA2KTgeAijBNrmvdSjo+F\nzd9e+SCGHJTQx9UvdyUgmQnHSWBBFqnm4hv5byC7QgDjkkAJ2s+ejh6If+xBuJhW\nigMScpUUoeAOO9Ix9dS4Khfs\n-----END PRIVATE KEY-----\n",
  "client_email": "storage-operator@kubeflow-test-306307.iam.gserviceaccount.com",
  "client_id": "111346110221609971267",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/storage-operator%40kubeflow-test-306307.iam.gserviceaccount.com"
    }
    print(data)
    
    mg=MongoDBOperation()
    mg.insert_record_in_collection("Credentials","gcp",data)
    """
    #from entity_layer.registration.registration import Register
    #reg=Register()

    mg = MongoDBOperation()
    mg.insert_dataframe_into_collection("anvihs", "yadav avnish", pd.DataFrame({'id':[1,2,3,]}))
    print('hi')
    #print(reg.add_user_role('viewer'))
    """
    update_value={'last_name':'Yadav'}
    update_query={'$set':update_value}
    mg.update_record_in_colleciton("update_test","update_collection",{'user_id':123},update_query)
    """
except Exception as e:
    print(e)
    exc_type, exc_obj, exc_tb = sys.exc_info()
    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_tb.tb_lineno,file_name)