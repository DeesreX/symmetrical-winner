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
        self.equation = ""

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        print(a, b)
        return a * b

    def divide(self, a, b):
        return a / b

    def calculate(self, equation):
        self.equation = equation
        while self.contains_operation(self.equation):
            self.equation = self.calculate_equation(self.equation)

        return self.equation

    def calculate_equation(self, equation):
        self.get_operations(equation)
        equation = equation.replace(" ", "")
        rearranged = self.rearrange_operations()
        print(rearranged)
        to_find = rearranged[0]
        left = to_find.split(to_find[1])[0]
        right = to_find.split(to_find[1])[1]
        to_replace_value = self.operators[to_find[1]]
        equation = equation.replace(to_find, str(to_replace_value(int(left), int(right))))
        return equation

    def rearrange_operations(self):
        new_stack = []
        for operation in self.stack:
            print(operation + " OPERATION")
            if operation[1] == '*' or operation[1] == '/':
                new_stack.insert(0, operation)
            else:
                new_stack.insert(-1, operation)

        return new_stack



    def contains_operation(self, equation):
        for operation in list(equation):
            if operation in self.operators:
                return True
        return False

    def get_operations(self, equation):
        self.stack = []
        for i, char in enumerate(equation.split(" ")):
            if char in self.operators:
                operation = equation.split(" ")[i - 1] + char + equation.split(" ")[i + 1]
                self.stack.append(operation)
                print("STACK: " + str(self.stack))

if __name__ == "__main__":
    calculator = BasicCalculator()
    cal_1 = "1 + 2"
    cal_2 = "2 + 5 * 10"
    

    result = calculator.calculate(cal_2)
    print("Answer = " + result)