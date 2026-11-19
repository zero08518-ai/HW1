import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()

        result = func(*args, **kwargs)

        end = time.perf_counter()

        print(f"Час роботи: {end - start:.8f} секунд")

        return result

    return wrapper


@timer
def calculate(a, b):
    return a + b