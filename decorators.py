from functools import wraps
import requests


def error_handler(func):
    """
    A decorator that wraps a function to handle exceptions raised by the `requests` library.

    This decorator catches and handles the following exceptions:
    - requests.exceptions.HTTPError
    - requests.exceptions.ConnectionError
    - requests.exceptions.Timeout
    - requests.exceptions.RequestException

    If an exception is caught, an appropriate error message is printed, and an empty dictionary is returned.

    Args:
        func (callable): The function to be wrapped by the decorator.

    Returns:
        callable: The wrapped function with error handling.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
        except requests.exceptions.RequestException as req_err:
            print(f"An error occurred: {req_err}")
        return {}

    return wrapper
