from zipfile import ZipFile
import os
PATH = "D:\\Project\\"

projects=os.listdir(path=PATH)
DESTINATION_PATH=r"E:\MEGA-CHALLANGE-INEURON"

if os.path.exists(DESTINATION_PATH):
    print("Directory [{}] found".format(DESTINATION_PATH))
else:
    print("Directory [{}] not found".format(DESTINATION_PATH))
    os.mkdir(DESTINATION_PATH)
    print("Directory [{}] created ".format(DESTINATION_PATH))
for project in projects:
    print(PATH+project)
    with ZipFile(PATH+project) as f:
        f.extractall(path=DESTINATION_PATH)




