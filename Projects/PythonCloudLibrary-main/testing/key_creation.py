from encryption.encrypt_confidential_data import EncryptData

ed=EncryptData()

encrypted_send_email=ed.encrypt_message("machine.learning.application@gmail.com").decode('utf-8')
print("encrypted_send_email:{}".format(encrypted_send_email))

encrypted_send_email_password=ed.encrypt_message("Aa908990@").decode('utf-8')
print("encrypted_send_email_password:{}".format(encrypted_send_email_password))
