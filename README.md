# Calculator
A small Python calculator library for basic arithmetic operations.

## Features
- calculating simple math (+, -, *, /, **, %)
- usage as a library in another file
- Three additional Python files to test the library and its functionality
- A CLI for simple and fast usage

## Technologies
- Python
- Tkinter (Included in python)
- Python Package

## Installation
1. Install at least Python 3.14.7  ([Python 3.14.7 Windows 64-bit installer](https://www.python.org/ftp/python/3.14.7/python-3.14.7-amd64.exe) | [Windows 3.14.7 32-bit installer](https://www.python.org/ftp/python/3.14.7/python-3.14.7.exe) | [Python 3.14.7 macOS installer](https://www.python.org/ftp/python/3.14.7/python-3.14.7-macos11.pkg) | [All releases](https://www.python.org/downloads/))
2. Run: ``` py -m pip install git+https://github.com/alessioiskuhl/Calculator.git ``` in the terminal of your choice

## Library usage
### CLI
1. Open a terminal of your choice
2. Make a calculation with the following format: ` calculator <number> <operator> <number> `

### Inside a script
1. Type ` from calculator import Calculator ` at the beginning of your script to import the library into your script or use one of the three test scripts
2. Assign an object to the class from the Calculator library
3. Use the following format to perform a calculation: yourObject.calc(float(firstNumber), mathExpressionAsString, float(secondNumber))

**Example Use:**
```Python
from calculator import Calculator    # Import the library

calc = Calculator()                  # Create an object for the Calculator class

result = calc.calc(10, "+", 5)       # Calculates the result

print(result)                        # Prints out the result (should be 15 in this case)
```
or for a calculator with text input:
```Python
from calculator import Calculator                                                                         # Importing the library

calc = Calculator()                                                                                       # Create an object for the Calculator class

calculation = input("Enter your calculation in the format: num1 operation num2 (e.g., 5 + 3): ")          # Asking for user input and saving it in a variable

num1, types, num2 = calculation.split()                                                                   # Splits the user input into 3 different variables to put into the calculation function

print(calc.calc(float(num1), types, float(num2)))                                                         # Calculates and prints the result
```

## Test usage
> [!NOTE]
> It may be that if you double click the file instead of running it in a terminal, that you will just see a window appear for a split second. This is because python closes the command window that opened as soon as the script is done running. It is recommended to run the test files via a terminal like cmd. This does not apply to the test with UI.
### automated test
Running the file should output something like in the following picture if you have installed the library correctly:

<img width="363" height="202" alt="Screenshot 2026-08-27 225342" src="https://github.com/user-attachments/assets/78cd70ad-d99e-4708-ab8b-0013dd513442" />



### simple text test
When running the simple text test it should work like a simple command line calculator if you have installed everything correctly

### test with UI
When running this file, a simple window should open letting you type in the numbers, select a math operation and press a button to calculate and show the result. If you have Python installed (Which you need for this calculator) you should not need to install anything additional to be able to use the test with UI.


## What I learned
- You can import a class from another python file into your script basically turning it into a library
- When importing a class into your script yoou need to make sure every function inside the class has **self** as the first expression to avoid problems at usage
- Proper file organization on GitHub
- Turning a python file into a proper library installable with git clone
- Creating a CLI

> [!NOTE]
> This project was created with the help of AI, although I only used AI for learning structure, python packages etc. not for the coding
