from Calculator import Calculator


performance = input("What operation would you like to perform?(calculator, exit): ")
if performance == "calculator":
    calc = Calculator()
    calculation = input("Enter your calculation in the format: num1 operation num2 (e.g., 5 + 3): ")
    num1, types, num2 = calculation.split()
    print(calc.calc(float(num1), types, float(num2)))
elif performance == "exit":
    print("Exiting the program.")
else:
    print("Invalid input. Please enter 'calculator' or 'exit'.")
