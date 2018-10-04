import datetime
import time

def log_performance(func):
    def wrapper(*args, **kwargs):
        datetime_now = datetime.datetime.now()
        print(f"Function {func.__name__} being called at : {datetime_now}")
        start_time = time.time()

        result = func(*args, **kwargs)

        print(f"Took {time.time() - start_time} seconds")
        return result
    return wrapper


@log_performance
def calculate_squares(n):
    for i in range(n):
        i_squared = i**2


if __name__ == '__main__':
    calculate_squares(10_000_000)
