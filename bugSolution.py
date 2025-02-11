def function(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None

result = function(10, 0)
result2 = function(10,2) 
print(result2) #prints 5.0