from Calculator import Calculator

calc = Calculator()
calculation = input("Enter your calculation in the format: num1 operation num2 (e.g., 5 + 3): ")
num1, types, num2 = calculation.split()
print(calc.calc(float(num1), types, float(num2)))