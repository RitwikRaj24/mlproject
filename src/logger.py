# any execution that happens , you should be able to log all those information into a file so that we are able to track any errors along the way 

import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # text file will get created in this naming convention 
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) # path where the logs will be stored 
os.makedirs(logs_path,exist_ok=True) # exist_ok -> even if there is a file , keep appending on to it 

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", # how the message will be printed
    level=logging.INFO) # specifying level 

# if __name__ == '__main__': # checking if the code above works or not
#     logging.info("Logging has started")