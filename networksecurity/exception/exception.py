import sys
from networksecurity.logging import logger
class NetworkSecurityException(Exception):
    def __init__(self,error_message,error_details:sys):
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()

        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return f"Error: {self.error_message} at line {self.lineno} in {self.file_name}"
    

if __name__ == "__main__":
    try:
        logger.logging.info("this is a test log")
        a=1/0
        print("this will not be printed",a)
    except Exception as e:  
            raise NetworkSecurityException(e,sys)