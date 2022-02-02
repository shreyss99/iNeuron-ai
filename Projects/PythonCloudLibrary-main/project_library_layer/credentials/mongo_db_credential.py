#from encryption.encrypt_confidential_data import EncryptData
from entity_layer.encryption.encrypt_confidential_data import EncryptData

def get_mongo_db_credentials():
    encrypt_data=EncryptData()
    encrypted_user_name="gAAAAABgcjkwodrRTetyw64aDBSvjuu-ukf3aDn8rDlnrQPZdMTrq" \
              "\VbkCXUs8lfCTrxNrrL9jVVVlFOPh39AA_daB1VXaK1ofw==".encode('utf-8')
    encrypted_password="gAAAAABgcjkwtMylC8RHjcB9EpYNyFjHrZt1Y8Nv-aQsygzQUluKmaJyOu" \
             "R7mgWdF_XyO_AjVQ0-duduOujUaJBLwuPDVe7WlA==".encode('utf-8')
    user_name=encrypt_data.decrypt_message(encrypted_user_name).decode('utf-8')
    password=encrypt_data.decrypt_message(encrypted_password).decode('utf-8')
    return {'user_name': user_name, 'password': password}

"""
encrypt_data=EncryptData()
encrypted_send_email=encrypt_data.encrypt_message("machine.learning.application@gmail.com").decode('utf-8')
print("encrypted_send_email:{}".format(encrypted_send_email))

encrypted_send_email_password=encrypt_data.encrypt_message("Aa908990@").decode('utf-8')
print("encrypted_send_email_password:{}".format(encrypted_send_email_password))
"""




