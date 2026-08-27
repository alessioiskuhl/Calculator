from calculator import Calculator

print("Running automated tests for the Calculator class...")

class bcolor:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def test_calculator_addition():
    calc = Calculator()
    result = calc.calc(2, '+', 3)
    if result == "Result: 5":
        print(f"{bcolor.OKGREEN}Addition test passed.{bcolor.ENDC}")
    else:
        print(f"{bcolor.FAIL}Addition test failed.{bcolor.ENDC}")
        raise AssertionError(f"Expected 'Result: 5', but got {result}")

def test_calculator_modulo():
    calc = Calculator()
    result = calc.calc(10, 'mod', 3)
    if result == "Result: 1":
        print(f"{bcolor.OKGREEN}Modulo test passed.{bcolor.ENDC}")
    else:
        print(f"{bcolor.FAIL}Modulo test failed.{bcolor.ENDC}")
        raise AssertionError(f"Expected 'Result: 1', but got {result}")

def test_calculator_division_by_zero():
    calc = Calculator()
    result = calc.calc(10, '/', 0)
    if result == "Error: Division by zero is not allowed.":
        print(f"{bcolor.OKGREEN}Division by zero test passed.{bcolor.ENDC}")
    else:
        print(f"{bcolor.FAIL}Division by zero test failed.{bcolor.ENDC}")
        raise AssertionError(f"Expected error message, but got {result}")
def test_calculator_invalid_operation():
    calc = Calculator()
    result = calc.calc(10, 'invalid', 5)
    if result == "Error: Invalid operation type. Please enter a valid operation (+, -, *, /, **, %) or (add, subtract, multiply, divide, power, mod).":
        print(f"{bcolor.OKGREEN}Invalid operation test passed.{bcolor.ENDC}")
    else:
        print(f"{bcolor.FAIL}Invalid operation test failed.{bcolor.ENDC}")
        raise AssertionError(f"Expected error message, but got {result}")

def test_calculator_power():
    calc = Calculator()
    result = calc.calc(2, '**', 3)
    if result == "Result: 8":
        print(f"{bcolor.OKGREEN}Power test passed.{bcolor.ENDC}")
    else:
        print(f"{bcolor.FAIL}Power test failed.{bcolor.ENDC}")
        raise AssertionError(f"Expected 'Result: 8', but got {result}")

def test_calculator_subtraction():
    calc = Calculator()
    result = calc.calc(5, '-', 3)
    if result == "Result: 2":
        print(f"{bcolor.OKGREEN}Subtraction test passed.{bcolor.ENDC}")
    else:
        print(f"{bcolor.FAIL}Subtraction test failed.{bcolor.ENDC}")
        raise AssertionError(f"Expected 'Result: 2', but got {result}")

def test_calculator_multiplication():
    calc = Calculator()
    result = calc.calc(4, '*', 5)
    if result == "Result: 20":
        print(f"{bcolor.OKGREEN}Multiplication test passed.{bcolor.ENDC}")
    else:
        print(f"{bcolor.FAIL}Multiplication test failed.{bcolor.ENDC}")
        raise AssertionError(f"Expected 'Result: 20', but got {result}")

def test_calculator_modulo_by_zero():
    calc = Calculator()
    result = calc.calc(10, 'mod', 0)
    if result == "Error: Modulo by zero is not allowed.":
        print(f"{bcolor.OKGREEN}Modulo by zero test passed.{bcolor.ENDC}")
    else:
        print(f"{bcolor.FAIL}Modulo by zero test failed.{bcolor.ENDC}")
        raise AssertionError(f"Expected error message, but got {result}")

def test_calculator_float_addition():
    calc = Calculator()
    result = calc.calc(2.5, '+', 3.1)
    if result == "Result: 5.6":
        print(f"{bcolor.OKGREEN}Float addition test passed.{bcolor.ENDC}")
    else:
        print(f"{bcolor.FAIL}Float addition test failed.{bcolor.ENDC}")
        raise AssertionError(f"Expected 'Result: 5.6', but got {result}")

def test_calculator_float_division():
    calc = Calculator()
    result = calc.calc(5.0, '/', 2.0)
    if result == "Result: 2.5":
        print(f"{bcolor.OKGREEN}Float division test passed.{bcolor.ENDC}")
    else:
        print(f"{bcolor.FAIL}Float division test failed.{bcolor.ENDC}")
        raise AssertionError(f"Expected 'Result: 2.5', but got {result}")

try:
    test_calculator_addition()
    test_calculator_modulo()
    test_calculator_division_by_zero()
    test_calculator_invalid_operation()
    test_calculator_power()
    test_calculator_subtraction()
    test_calculator_multiplication()
    test_calculator_modulo_by_zero()
    test_calculator_float_addition()
    test_calculator_float_division()

    print(f"{bcolor.OKGREEN}All tests passed successfully!{bcolor.ENDC}")
except Exception as e:
    print(f"{bcolor.FAIL}Test failed, the following error occurred: {e}{bcolor.ENDC}")