class BasicCalculator:
    def __init__(self):
        self.stack = []
        self.operators = {
            '*': self.multiply,
            '/': self.divide,
            '+': self.add,
            '-': self.subtract
        }
        self.operations = {}

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

    def calculate(self, equation):
        # find all operations containing * and /
        for i, char in enumerate(equation):
            if char in self.operators:
                operator = self.operators[char]
                self.operations[i] = [char, equation[i-1], equation[i+1], operator]


        for i, operation in self.operations.items():
            result = operation[3](int(operation[1]), int(operation[2]))
            to_replace = operation[1] + operation[0] + operation[2]
            equation = equation.replace(to_replace, str(result))
        
        return equation