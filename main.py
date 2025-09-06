def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
if __name__ == "__main__":
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))

    print(f"Sum: {add(n1, n2)}")
    print(f"Difference: {subtract(n1, n2)}")
    print(f"Product: {multiply(n1, n2)}")
