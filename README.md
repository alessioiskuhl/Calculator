# Calculator
A small python calculator

## Features
- calculating simple math (+, -, *, /, **)
- usage as a library in another file
- A second python file to test the library

## Technologies
- Python

## Installation
1. Click on the green Code button above the files
2. Press "Download ZIP"
3. Export the ZIP file and put Calculator.py in the destination folder where the script needing the Calculator library lies
4. Type ` from Calculator import Calculator ` at the beginning of your script to import the library into your script

## Usage
1. Assign an object to the class from the Calculator library
2. Use the following format to perform a calculation: yourObject.calc(float(firstNumber), mathExpressionAsString, float(secondNumber))

**Example Use:**
```
from Taschenrechner import Calculator

calc = Calculator()
calculation = input("Enter your calculation in the format: num1 operation num2 (e.g., 5 + 3): ")
num1, types, num2 = calculation.split()
print(calc.calc(float(num1), types, float(num2)))
```

## What I learned
- You can import a class from another python file into your script basically turning it into a library
- When importing a class into your script yoou need to make sure every function inside the class has **self** as the first expression to avoid problems at usage

## TODO
- Add a simple UI into the example file using PyQt5 to make usage after implementation easier
