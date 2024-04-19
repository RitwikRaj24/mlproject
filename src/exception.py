import sys # provides various functions and variables that are used to manipulate different parts of the Python runtime environment
from src.logger import logging

def error_message_detail(error, error_detail:sys): # whenever an error is raised , push this custom message 
    _,_,exc_tb = error_detail.exc_info() # 'exc_info()' = execution info , from which the third file is required which has been assigned to variable exc_tb 
    # exc_tb will have information like which file , line etc. the exception has occured 

    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = f"Error occured in python script {file_name} line number {exc_tb.tb_lineno} error_message {str(error)}"

    return error_message # whenever an error is raised , this function gets called 

class CustomException(Exception): # create customexception class which is inheriting from Exception 
    def __init__(self, error_message, error_detail:sys): 
        super().__init__(error_message) # overriddent the init method 
        self.error_message = error_message_detail(error_message, error_detail=error_detail) # created error_message variable 

    def __str__(self): 
        return self.error_message # when called to print 


# if __name__ == "__main__": # checking to see if the program above is working 
#     try:
#         a = 1/0 
#     except Exception as e:
#         logging.info("Divide by Zero")
#         raise CustomException(e,sys)