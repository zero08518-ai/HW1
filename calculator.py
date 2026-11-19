
def checker(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception as exc:
            print(f"Помилка: {exc}")
        else:
            print(f"Результат: {result}")

    return wrapper


@checker
def calculate(expression):
    return eval(expression, {"__builtins__": {}}, {})


while True:
    expression = input("Завдання або 'exit': ")

    if expression == "exit":
        break

    calculate(expression)
