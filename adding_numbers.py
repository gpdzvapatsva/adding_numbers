#import the 'tkinter module
from tkinter import*
root = Tk() # Blank window
root.geometry("550x350")
#adding a background colour
root.config(bg='yellow')
#create the title for the window
root.title("Adding two numbers")


#creating label widgets
label1 = Label(root, text = "Please enter first number:");
label2 = Label (root, text = "Please enter second number:")
label3 = Label(root, text="Your answer:")
label4=Label(root)
#Positioning the input & output fields
first_num = Entry (root )
second_num = Entry(root)
answer = Entry(root)

#functions
def button_clear ():
    #CLEARING THE INPUT FIELDS
    answer.delete(0, END)
    first_num.delete(0,END)
    second_num.delete(0,END)

def button_add ():
    # SUM OF THE TWO NUMBERS
    digit_1 = first_num.get();
    digit_2 = second_num.get();
    first_add = int(digit_1)
    second_add = int (digit_2)
    answer.insert(0, first_add + second_add)

def button_exit ():
    # EXITING
    import sys
    sys.exit()
    # exits the program
    #sys.exit("Age less than 18")

# Buttons
button_add = Button(root,  borderwidth=10, font=("Consolas 15 bold"),text="Add", bg="purple", fg="white", width=10, command=button_add)
button_clear = Button(root, text="Clear", borderwidth=10, font=("Consolas 15 bold"), bg="purple", fg="white", width=10, command=button_clear)
button_exit = Button(root, text="Exit", borderwidth=10, font=("Consolas 15 bold"), bg="purple", fg="white", width=10, command=button_exit)

#display
label1.grid(row=0, column=0, padx=10, pady=10 )
label2.grid(row=1,column=0, padx=10, pady=10)
label3.grid(row=2,column=0, padx=10, pady=10)
first_num.grid(row=0,column=1, padx=10, pady=10)
second_num.grid(row=1,column=1, padx=10, pady=10)
answer.grid(row=2,column=1, padx=10, pady=10)
#button_add.place(row=3,column=1, padx=2, pady=10)
button_add.place(x=20, y=150)
button_clear.place(x=200, y=150)
button_exit.place(x=380, y=150)
root.mainloop()