import sys
from .calculator import Calculator

def main():
    if len(sys.argv) != 4:
        print("Usage: calculator <number> <operator> <number>")
        return

    a = float(sys.argv[1])
    operator = sys.argv[2]
    b = float(sys.argv[3])

    calculator = Calculator()
    print("You are currently using Alessio-Calculator")
    print(calculator.calc(a, operator, b))