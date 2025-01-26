from src.logger import logging

def exception_handler(error, error_detail):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred in file [{file_name}] at line [{exc_tb.tb_lineno}]: {str(error)}"
    logging.error(error_message)
    raise Exception(error_message)