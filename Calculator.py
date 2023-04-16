from tkinter import * # This imports all the classes, functions, and constants from the tkinter module.

# -------------Defining the GUI structure-------------
calculatorGui = Tk() # This creates a new instance of the Tk class, which represents the main window of the GUI application.

calculatorGui.title("Python(tkinter) - Calculator by MAP")  # This sets the title of the GUI window

calculatorGui.geometry("570x613") # This sets the size of the GUI window to 570 pixels wide and 613 pixels tall.

calculatorGui.resizable(FALSE, FALSE) # This prevents from resizing the window

calculatorGui.config(background="#1a1a19",) # Giving GUI background color



# -------------Actual logic of calculator starts from here-------------

def click(event): # This functions performs different operations on numbers except square & cube

    global screenValue
    
    if display.get() == "ERROR": # Will automatically clear the display if Error is generated in previous calculations
        screenValue.set("")
        display.update()
    elif display.get() == "Can't divide by Zero":
        screenValue.set("")
        display.update()
    
    text = event.widget.cget("text") # This allows the calculator program to determine which button was pressed and perform the appropriate action based on the value of the button.

    if text == "=": # if "=" button is clicked, it will evaluate the expression on the display
        if screenValue.get().isdigit():
            value = int(screenValue.get())
        else:
            try: 
                value = eval(screenValue.get())
            except ZeroDivisionError as zero:
                value="Can't divide by Zero"
            except Exception as e:
                value = "ERROR"
        screenValue.set(value)
        display.update() # updating the display with the result
        
    elif text == "C": # if "C" button is clicked, it will clear the display

        screenValue.set("")
        display.update()
    
    elif text == "<": # if "<" button is clicked, it will erase the last char of expression on the display
        screenValue.set(screenValue.get()[:-1])
        display.update()
    elif text == "π": # if "π" button is clicked, it will print the value of pi on the display
        screenValue.set(screenValue.get() + f"{22/7}")
        display.update()
    else: # Except all above, if any other button is clicked, it will be appended to the expression on the display
        screenValue.set(screenValue.get() + text)
        display.update()
    
    
def click2(event): # This functions performs square & cube operation on numbers 

    text2 = event.widget.cget("text") # Getting the button text in a variable
    
    if screenValue.get().isdigit():
        int(screenValue.get())
        
    # Formula of square and cube storing in a variable
    square = (int(screenValue.get()) * int(screenValue.get()))
    cube = (int(screenValue.get()) * int(screenValue.get()) * int(screenValue.get()))

    # Square and cube button output
    if text2 == "x²":
        screenValue.set(square)
        display.update()

    elif text2 == "x³":
        screenValue.set(cube)
        display.update()


# -------------Creating Monitor (DISPLAY)-------------

screenValue = StringVar() # StringVar is a special variable used to store string values that can be updated and traced.

display = Entry(calculatorGui, textvariable=screenValue,
                font=("times new roman", 38, "bold"),
                borderwidth=2,relief=SUNKEN) # Creating main frame display where i/o will be displayed

display.pack(padx=10,pady=10,ipady=15) # This adds the text entry field to the GUI window using the pack() geometry manager, which automatically arranges widgets in a vertical or horizontal stack.


# -------------Creating Buttons------------
btns = Button(calculatorGui, text="C", font="arial 20 bold",
              height=2, width=7, bd=2, fg="white", bg="red", relief=GROOVE)
btns.place(x=3, y=120)
btns.bind("<Button-1>", click) # This binds a mouse click event to the click function for the button, using the <Button-1> event code.


btns = Button(calculatorGui, text="%", font="arial 20 bold",
              height=2, width=4, bd=2, fg="black", bg="#FFFF33", relief=GROOVE)
btns.place(x=140, y=120)
btns.bind("<Button-1>", click)

btns = Button(calculatorGui, text="x²", font="arial 20 bold",
              height=2, width=4, bd=2, fg="black", bg="#FFFF33", relief=GROOVE)
btns.place(x=225, y=120)
btns.bind("<Button-1>", click2)

btns = Button(calculatorGui, text="x³", font="arial 20 bold",
              height=2, width=4, bd=2, fg="black", bg="#FFFF33", relief=GROOVE)
btns.place(x=312, y=120)
btns.bind("<Button-1>", click2)

btns = Button(calculatorGui, text="π", font="arial 20 bold",
              height=2, width=4, bd=2, fg="black", bg="#FFFF33", relief=GROOVE)
btns.place(x=399, y=120)
btns.bind("<Button-1>", click)

btns = Button(calculatorGui, text="-", font="arial 20 bold",
              height=2, width=4, bd=2, fg="black", bg="#FFFF33", relief=GROOVE)
btns.place(x=485, y=120)
btns.bind("<Button-1>", click)

btns = Button(calculatorGui, text="9", font="arial 20 bold",
              height=2, width=7, bd=2, fg="white", bg="#40403f", relief=GROOVE)
btns.place(x=3, y=220)
btns.bind("<Button-1>", click)

btns = Button(calculatorGui, text="8", font="arial 20 bold",
              height=2, width=7, bd=2, fg="white", bg="#40403f", relief=GROOVE)
btns.place(x=140, y=220)
btns.bind("<Button-1>", click)

btns = Button(calculatorGui, text="7", font="arial 20 bold",
              height=2, width=7, bd=2, fg="white", bg="#40403f", relief=GROOVE)
btns.place(x=278, y=220)
btns.bind("<Button-1>", click)

btns = Button(calculatorGui, text="+", font="arial 20 bold",
              height=2, width=8, bd=2, fg="black", bg="#FFFF33", relief=GROOVE)
btns.place(x=418, y=220)
btns.bind("<Button-1>", click)

btns = Button(calculatorGui, text="6", font="arial 20 bold",
              height=2, width=7, bd=2, fg="white", bg="#40403f", relief=GROOVE)
btns.place(x=3, y=320)
btns.bind("<Button-1>", click)

btns = Button(calculatorGui, text="5", font="arial 20 bold",
              height=2, width=7, bd=2, fg="white", bg="#40403f", relief=GROOVE)
btns.place(x=140, y=320)
btns.bind("<Button-1>", click)

btns = Button(calculatorGui, text="4", font="arial 20 bold",
              height=2, width=7, bd=2, fg="white", bg="#40403f", relief=GROOVE)
btns.place(x=278, y=320)
btns.bind("<Button-1>", click)

btns = Button(calculatorGui, text="*", font="arial 20 bold",
              height=2, width=8, bd=2, fg="black", bg="#FFFF33", relief=GROOVE)
btns.place(x=418, y=320)
btns.bind("<Button-1>", click)

btns = Button(calculatorGui, text="3", font="arial 20 bold",
              height=2, width=7, bd=2, fg="white", bg="#40403f", relief=GROOVE)
btns.place(x=3, y=420)
btns.bind("<Button-1>", click)

btns = Button(calculatorGui, text="2", font="arial 20 bold",
              height=2, width=7, bd=2, fg="white", bg="#40403f", relief=GROOVE)
btns.place(x=140, y=420)
btns.bind("<Button-1>", click)

btns = Button(calculatorGui, text="1", font="arial 20 bold",
              height=2, width=7, bd=2, fg="white", bg="#40403f", relief=GROOVE)
btns.place(x=278, y=420)
btns.bind("<Button-1>", click)

btns = Button(calculatorGui, text="/", font="arial 20 bold",
              height=2, width=8, bd=2, fg="black", bg="#FFFF33", relief=GROOVE)
btns.place(x=418, y=420)
btns.bind("<Button-1>", click)

btns = Button(calculatorGui, text="=", font="arial 20 bold",
              height=2, width=8, bd=2, fg="black", bg="#87F717", relief=GROOVE)
btns.place(x=418, y=518)
btns.bind("<Button-1>", click)

btns = Button(calculatorGui, text="<", font="arial 20 bold", height=2,
              width=7, bd=2, fg="white", bg="#3697f5", relief=GROOVE)
btns.place(x=279, y=518)
btns.bind("<Button-1>", click)

btns = Button(calculatorGui, text=".", font="arial 20 bold",
              height=2, width=7, bd=2, fg="white", bg="#40403f", relief=GROOVE)
btns.place(x=140, y=518)
btns.bind("<Button-1>", click)

btns = Button(calculatorGui, text="0", font="arial 20 bold", height=2,
              width=7, bd=2, fg="white", bg="#40403f", relief=GROOVE)
btns.place(x=3, y=518)
btns.bind("<Button-1>", click)

calculatorGui.mainloop() # This will keep the window active and responsive. Without the mainloop() call, the window would be created but would not respond to user input or update its display
