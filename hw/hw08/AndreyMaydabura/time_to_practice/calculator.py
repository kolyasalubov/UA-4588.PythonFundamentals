import mymath

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Choose operation (+, -, *, /): ")

if operation == "+":
    result = mymath.add(a, b)
elif operation == "-":
    result = mymath.subtract(a, b)
elif operation == "*":
    result = mymath.multiply(a, b)
elif operation == "/":
    result = mymath.divide(a, b)
else:
    result = "Unknown operation"

print("Result:", result)


# operations = {
#     "+": mymath.add,
#     "-": mymath.subtract,
#     "*": mymath.multiply,
#     "/": mymath.divide,
# }

# result = operations.get(operation)

# if result:
#     print("Result:", result(a, b))
# else:
#     print("Unknown operation")
