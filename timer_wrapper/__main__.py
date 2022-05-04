from datetime import datetime
from time import sleep

def timed_run(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        time_diff = round((end_time - start_time).total_seconds() * 1000)
        print(f"{func.__name__} execution terminated in {time_diff} ms." )
        return result
    return wrapper

@timed_run
def print_hello():
    print("Hello")

if __name__ == '__main__':
    print_hello()