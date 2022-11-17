"""The entry point of the calculator."""

from basic_calculator import basic_calculator

def main():
    """The entry point of the calculator."""
    calculator = basic_calculator.BasicCalculator()
    result = calculator.calculate("1+2*3")
    print(result)

if __name__ == "__main__":
    main()