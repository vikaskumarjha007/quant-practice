# main.py - first interactive program

def numbers():
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))

    total = number1 + number2
    print(f"The sum of {number1} and {number2} is {total}") 

    difference = number1 - number2
    print(f"The difference of {number1} and {number2} is {difference}")

    product = number1 * number2
    print(f"The product of {number1} and {number2} is {product}")

    print(f"The quotient of {number1} and {number2} is {number1 / number2}")

if __name__ == "__main__":
    numbers()
