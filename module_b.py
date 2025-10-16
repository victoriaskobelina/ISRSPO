def risky_function(value):
    if value < 0:
        raise ValueError("Значение не может быть отрицательным")
    return value * 2
