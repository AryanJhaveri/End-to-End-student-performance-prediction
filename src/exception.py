import sys

def error_message_details(error, error_deail:sys):
    _,_, exc_tb = error_deail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "error occured in python script name [{0}]  line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    
    return error_message
    
class CustomEception(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_deail=error_detail)
        
    def __str__(self):
        return self.error_message