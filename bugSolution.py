def function(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero!"

result = function(10, 0)
print(result)