###########################################################################
#
#       Name:Songrui Li
#       Project: GUI Calculator
#       12/10/2016
#
#
###########################################################################


import tkinter as tk
import parser

root = tk.Tk()
root.title('Calculator')

###### Constants
##
FONT_LARGE = ("Calibri", 12)      ## selects the font of the text inside buttons
FONT_MED = ("Calibri", 10)
MAX_ROW = 4                        ## Max rows and columns in the GUI
MAX_COLUMN = 5
i = 0       ## for the insertion counter in Entry widget
###############

def factorial(operator):
    """Calculates the factorial of the number entered."""
    number = int(display.get())
    fact = 1
    try:
        while number > 0:
            fact = fact*number
            number -= 1
        clear_all()
        display.insert(0, fact)
    except Exception:
        clear_all()
        display.insert(0, "Error")


def clear_all():
    """clears all the content in the Entry widget"""
    display.delete(0, tk.END)

def log(btn):
    f = open("log.txt", "a")
    f.write(str(btn))
    f.close()
    
def get_variables(num):
    """Gets the user input for operands and puts it inside the entry widget"""
    global evaluated, i
    if evaluated:
        clear_all()
    evaluated = False
    display.insert(i, num)
    i += 1
    log(num)

def get_operation(operator):
    """Gets the operand the user wants to apply on the functions"""
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length
    log(operator)

def undo():
    """removes the last entered operator/variable from entry widget"""
    whole_string = display.get()
    if len(whole_string):        ## repeats until
        ## now just decrement the string by one index
        new_string = whole_string[:-1]
        print(new_string)
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all() 
        display.insert(0, "Error, press AC")

def calculate():
    """
    Evaluates the expression
    ref : http://stackoverflow.com/questions/594266/equation-parsing-in-python
    """
    global evaluated

    whole_string = display.get()
    try:
        formulae = parser.expr(whole_string).compile()
        result = eval(formulae)
        clear_all()
        display.insert(0, result)
        log("="+str(result)+"\n")
        evaluated = True

    except Exception:
        clear_all()
        display.insert(0, "Error!")


for row in range(MAX_ROW):
    root.columnconfigure(row,pad=3)

for column in range(MAX_COLUMN):
    root.rowconfigure(column,pad=3)

display = tk.Entry(root, font = ("Calibri", 13))
display.grid(row = 1, columnspan = 6 , sticky = tk.W + tk.E )   

global evaluated
evaluated=False
one = tk.Button(root, text = "1", command = lambda : get_variables(1), font=FONT_LARGE)
one.grid(row = 2, column = 0)
two = tk.Button(root, text = "2", command = lambda : get_variables(2), font=FONT_LARGE)
two.grid(row = 2, column = 1)
three = tk.Button(root, text = "3", command = lambda : get_variables(3), font=FONT_LARGE)
three.grid(row = 2, column = 2)

four = tk.Button(root, text = "4", command = lambda : get_variables(4), font=FONT_LARGE)
four.grid(row = 3 , column = 0)
five = tk.Button(root, text = "5", command = lambda : get_variables(5), font=FONT_LARGE)
five.grid(row = 3, column = 1)
six = tk.Button(root, text = "6", command = lambda : get_variables(6), font=FONT_LARGE)
six.grid(row = 3, column = 2)

seven = tk.Button(root, text = "7", command = lambda : get_variables(7), font=FONT_LARGE)
seven.grid(row = 4, column = 0)
eight = tk.Button(root, text = "8", command = lambda : get_variables(8), font=FONT_LARGE)
eight.grid(row = 4, column = 1)
nine = tk.Button(root , text = "9", command = lambda : get_variables(9), font=FONT_LARGE)
nine.grid(row = 4, column = 2)

cls = tk.Button(root, text = "AC", command = clear_all, font=FONT_LARGE, foreground = "red")
cls.grid(row = 5, column = 0)
zero = tk.Button(root, text = "0", command = lambda : get_variables(0), font=FONT_LARGE)
zero.grid(row = 5, column = 1)
result = tk.Button(root, text = "=", command = calculate, font=FONT_LARGE, foreground = "red")
result.grid(row = 5, column = 2)

plus = tk.Button(root, text = "+", command =  lambda : get_operation("+"), font=FONT_LARGE)
plus.grid(row = 2, column = 3)
minus = tk.Button(root, text = "-", command =  lambda : get_operation("-"), font=FONT_LARGE)
minus.grid(row = 3, column = 3)
multiply = tk.Button(root,text = "*", command =  lambda : get_operation("*"), font=FONT_LARGE)
multiply.grid(row = 4, column = 3)
divide = tk.Button(root, text = "/", command = lambda :  get_operation("/"), font=FONT_LARGE)
divide.grid(row = 5, column = 3)


root.mainloop()
