import tkinter as tk
import tkinter.ttk as ttk


from Calculator import Calculator
calc = Calculator()
    

frame = tk.Tk() 
frame.title("Calculator") 
frame.geometry('200x250') 

Label_Zahl1 = tk.Label(frame, text="Enter 1st number:")
Label_Zahl1.place(x = 5, y = 5)

Entry_Zahl1 = tk.Entry(frame)
Entry_Zahl1.place(x = 5, y = 25)

Label_operation = tk.Label(frame, text="Enter operation (+, -, *, /, **):")
Label_operation.place(x = 5, y = 50)

operations = ["+", "-", "*", "/", "**"]
selected_operation = tk.StringVar()
Entry_operation = ttk.Combobox(frame, textvariable=selected_operation, values=operations)
Entry_operation.place(x = 5, y = 70)

Label_Zahl2 = tk.Label(frame, text="Enter 2nd number:")
Label_Zahl2.place(x = 5, y = 100)

Entry_Zahl2 = tk.Entry(frame)
Entry_Zahl2.place(x = 5, y = 120)

result_label = tk.Label(frame, text="Result: ")
result_label.place(x = 5, y = 180)

def calculate():
    try:
        num1 = float(Entry_Zahl1.get())
        operation = selected_operation.get()
        num2 = float(Entry_Zahl2.get())
        result = calc.calc(num1, operation, num2)
    except ValueError:
        result = "Error: Enter valid numbers."
    result_label.config(text=result)

Button_Calc = tk.Button(frame, text="Calculate", command=calculate)
Button_Calc.place(x = 5, y = 150)



frame.mainloop()
    