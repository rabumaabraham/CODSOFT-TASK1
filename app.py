class Calculator:

    def __init__(self, num1, num2, operator):
        self.num1 = num1
        self.num2 = num2
        self.operator = operator
        self.result = 0

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            return "Cannot divide by zero."

    def operation(self):
        if self.operator == '+':
            self.result = self.add()
        elif self.operator == '-':
            self.result = self.subtract()
        elif self.operator == '*' or self.operator == 'x':
            self.result = self.multiply()
        elif self.operator == '/':
            self.result = self.divide()
        else:
            self.result = "Invalid operator."
        return self.result

if __name__ == '__main__':
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            operator = input("Enter the operation (+, -, *, /): ").strip()
            num2 = float(input("Enter the second number: "))
            
            calculator = Calculator(num1, num2, operator)
            result = calculator.operation()
            
            print(f"{num1} {operator} {num2} = {result}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        
        continue_calculation = input("Do you want to continue calculation? (Y/N): ").strip().lower()
        if continue_calculation != 'y':
            break
