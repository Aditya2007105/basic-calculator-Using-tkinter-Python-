import tkinter

buttons = [
    ["AC", "+/-", "%", "/"],
    ["1", "2", "3", "*"],
    ["4", "5", "6", "-"],
    ["7", "8", "9", "+"],
    ["0", ".","Del", "="]
]

right_symbols = ["+", "-", "*", "/", "="] 
top_symbols = ["AC", "+/-", "%"]

row_count = len(buttons)
column_count = len(buttons[0])


colour_light_grey = "#D4D4D2"
colour_dark_grey = "#505050"
colour_orange = "#FF9500"
colour_white = "#FFFFFF"
colour_black = "#1C1C1C"

#window steup
window = tkinter.Tk()
window.title("Basic Calculator")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0", font=("Arial", 30), bg=colour_black,
                      fg=colour_white, anchor="e", width=column_count)
label.grid(row=0, column=0, columnspan=column_count, sticky="we")

for row in range(row_count):
    for column in range(column_count):
        value = buttons[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial", 30),
                                width=column_count-1, height=1,
                                command=lambda value=value: button_clicked(value))
        if value in top_symbols:
            button.config(fg=colour_black, bg=colour_light_grey)
        elif value in right_symbols:
            button.config(fg=colour_white, bg=colour_orange)
        else:
            button.config(fg=colour_white, bg=colour_dark_grey)
        button.grid(row=row+1, column=column)
frame.pack()

#Calculator logic
A = "0"
operator = None
B = None

def clear_all():
    global A, B, operator
    A = "0"
    B = None
    operator = None

def remove_zero_decimal(num):
    if num%1 == 0:
        num = int(num)
    return str(num)


def button_clicked(value):
    print("Pressed:", repr(value))
    global right_symbols, top_symbols, A, B, operator

    if value in right_symbols:
          print("INSIDE RIGHT_SYMBOLS")
          
          if value == "=":
            print("INSIDE EQUALS")
            if A is not None and operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)
                if operator == "+":
                    label["text"] = remove_zero_decimal(numA + numB)
                elif operator == "-":
                    label["text"] = remove_zero_decimal(numA - numB)
                elif operator == "*":
                    label["text"] = remove_zero_decimal(numA * numB)
                elif operator == "/":
                    label["text"] = remove_zero_decimal(numA / numB)
                    
                clear_all()
    if value in "+-*/":
        print("OPERATOR BLOCK ENTERED")
        A = label["text"]
        operator = value
        label["text"] = "0"

    elif value in top_symbols:
        if value == "AC":
            clear_all()
            label["text"] = "0"
        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)
        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)
    else: #digit or decimal point
        if value == ".":
            if value not in label["text"]:
                label["text"] += value
        elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value #replac 0 with the new digit
            else:
                label["text"] += value #append digit to the end of the current number


#Center the window on the screen
window.update_idletasks() #Update the window to get the correct width and height
width = window.winfo_width()
height = window.winfo_height()
x = (window.winfo_screenwidth() // 2) - (width // 2
)
y = (window.winfo_screenheight() // 2) - (height // 2)

#Set the geometry of the window to center it on the screen
#format "(w)x(h)+(x)+(y)"
window.geometry(f"{width}x{height}+{x}+{y}")


window.mainloop()
