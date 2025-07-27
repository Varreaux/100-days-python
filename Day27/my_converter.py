from tkinter import *

window = Tk()
window.title("my converter")
window.minsize(300,80)
window.focus_force()


miles_input = Entry(width=8)
miles_input.grid(row=0, column=1)
miles_input.focus()

miles_lable = Label(text="Miles")
miles_lable.grid(row=0,column=2)
miles_lable.config(padx=10)

equal_lable = Label(text="is equal to")
equal_lable.grid(row=1, column=0)
equal_lable.config(padx=20)

km_output = Label(text="0")
km_output.grid(row=1,column=1)

km_lable = Label(text="km")
km_lable.grid(row=1,column=2)

def calculate():
    km_output.config(text=str(round(float(miles_input.get())*1.60934, 2)))

button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)
window.bind("<Return>", lambda event: calculate())


window.mainloop()