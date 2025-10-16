from module_b import risky_function

def call_risky_function(value):
    try:
        result = risky_function(value)
        print(f"Результат: {result}")
    except ValueError as e:
        print(f"Обработка ошибки: {e}")
