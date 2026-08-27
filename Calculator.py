class Calculator:
    def calc(self, num1: float, types: str, num2: float):
        calc_type = 0
        if types == "+" or types == "add":
            calc_type = 1
        elif types == "-" or types == "subtract":
            calc_type = 2
        elif types == "*" or types == "multiply":
            calc_type = 3
        elif types == "/" or types == "divide":
            calc_type = 4
        elif types == "**" or types == "power":
            calc_type = 5
        result_msg = "Result: "
        if calc_type == 1:
            result = num1 + num2
            return result_msg + str(result)
        elif calc_type == 2:
            result = num1 - num2
            return result_msg + str(result)
        elif calc_type == 3:
            result = num1 * num2
            return result_msg + str(result)
        elif calc_type == 4:
            if num2 != 0:
                result = num1 / num2
                return result_msg + str(result)
            else:
                return "Error: Division by zero is not allowed."
        elif calc_type == 5:
            result = num1 ** num2
            return result_msg + str(result)
        else:
            return "Error: Invalid operation type. Please enter a valid operation (+, -, *, /, **) or (add, subtract, multiply, divide, power)."