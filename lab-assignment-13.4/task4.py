operation = input("Enter operation (add, subtract, multiply): ").strip()
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

operations = {
    "add": lambda x, y: x + y,
    "subtract": lambda x, y: x - y,
    "multiply": lambda x, y: x * y
}

result = operations.get(operation, lambda x, y: None)(a, b)
print(result)
