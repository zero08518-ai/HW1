import time
from timer import calculate, timer


@timer
def test_function():
    time.sleep(1)
    return True


assert calculate(2, 2) == 4
assert calculate(5, 5) == 10
assert calculate(10, 20) == 30
assert test_function() == True

print("Всі тести пройшли!")