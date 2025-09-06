# oop_calculator.py

class Calculator:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def add(self):
        return self.number1 + self.number2

    def subtract(self):
        return self.number1 - self.number2

    def multiply(self):
        return self.number1 * self.number2

    def divide(self):
        if self.number2 == 0:
            return "Error: Division by zero"
        return self.number1 / self.number2
    def power(self):
        return self.number1 ** self.number2
    def modulus(self):
        return self.number1 % self.number2
    
if __name__ == "__main__":
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))

    calc = Calculator(n1, n2)
    print(f"Sum: {calc.add()}")
    print(f"Difference: {calc.subtract()}")
    print(f"Product: {calc.multiply()}")
    print(f"Division: {calc.divide()}")
    print(f"Power: {calc.power()}")
    print(f"Modulus: {calc.modulus()}")
    