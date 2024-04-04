def add(x, y):
    """Function to add two numbers"""
    return x + y

print("Select operation:")
print("1. Add")

while True:
    choice = input("Enter choice (1): ")

    if choice == '1':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", add(num1, num2))
        break
    else:
        print("Invalid input")
