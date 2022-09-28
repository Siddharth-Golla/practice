from datetime import datetime
import time

# Time Function Decorator
def time_function(func):
    """Print the runtime of the decorated function"""
    def wrapper_time_function(*args, **kwargs):
        start_time = time.perf_counter()    
        return_value = func(*args, **kwargs)
        end_time = time.perf_counter()      
        run_time = end_time - start_time    
        print(f"Finished function {func.__name__} in {run_time:.8f} secs")
        return return_value
    return wrapper_time_function


# Log Function Decorator
def log_function(func):
    """Logs the function called in logfunction.txt and prints the time."""
    def wrapper_log_function(*args, **kwargs):
        return_value = func(*args, **kwargs)
        now = datetime.now()
        current_time = now.strftime("%d/%m/%Y %H:%M:%S")
        with open('logfunction.txt', 'a+') as file:
            func_name = func.__name__
            print(f"Function: {func_name} was called at {current_time}\n")
            file.write(f"Function: {func_name} was called at {current_time}\n")
        return return_value

    return wrapper_log_function

@time_function
@log_function
def fact(number):
    sum = 1
    for i in range(1, number + 1):
        sum = sum * i
    return sum


print(fact(100))