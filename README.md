# Calculator
A small Python calculator library for basic arithmetic operations.

## Features
- calculating simple math (+, -, *, /, **, %)
- usage as a library in another file
- A second python file to test the library

## Technologies
- Python
- Tkinter (Included in python)

## Installation
1. Click on the green Code button above the files
2. Press "Download ZIP"
3. Export the ZIP file and put Calculator.py (located in your extracted folder in the scripts folder) in the destination folder where the script needing the Calculator library lies
4. Type ` from Calculator import Calculator ` at the beginning of your script to import the library into your script or use one of the two test scripts

## Usage
1. Assign an object to the class from the Calculator library
2. Use the following format to perform a calculation: yourObject.calc(float(firstNumber), mathExpressionAsString, float(secondNumber))

**Example Use:**
```
from calculator import Calculator    # Import the library

calc = Calculator()                  # Create an object for the Calculator class

result = calc.calc(10, "+", 5)       # Calculates the result

print(result)                        # Prints out the result (should be 15 in this case)
```
or for a calculator with text input:
```
from Calculator import Calculator                                                                         # Importing the library

calc = Calculator()                                                                                       # Create an object for the Calculator class

calculation = input("Enter your calculation in the format: num1 operation num2 (e.g., 5 + 3): ")          # Asking for user input and saving it in a variable

num1, types, num2 = calculation.split()                                                                   # Splits the user input into 3 different variables to put into the calculation function

print(calc.calc(float(num1), types, float(num2)))                                                         # Calculates and prints the result
```

## What I learned
- You can import a class from another python file into your script basically turning it into a library
- When importing a class into your script yoou need to make sure every function inside the class has **self** as the first expression to avoid problems at usage
