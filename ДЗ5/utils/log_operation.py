import logging
from functools import wraps

logging.basicConfig(filename='ДЗ5/library_operations.log', level=logging.INFO, format='%(asctime)s -  %(message)s')

def log_operation(operation: str) -> any:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logging.info(f'Function for {operation} was called')
            result = func(*args, **kwargs)
            logging.info(f'Function for {operation} was finished')
            return result
        return wrapper
    return decorator