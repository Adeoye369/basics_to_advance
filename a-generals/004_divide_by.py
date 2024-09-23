def divide(a, b):
    try:
        return a / b
    
    except ZeroDivisionError:
        return "ZeroDivError:: Cannot have a divisor of Zero"

    except TypeError:
        return "TypeError::value must be integer or float"


print(divide(6, b = 2))
print(divide(12, 0))
print(divide(11, 34))
print(divide("112", 3))
print(divide(88, 12))