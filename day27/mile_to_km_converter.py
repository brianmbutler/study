from tkinter import *

window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=300, height=100)
#window.config(padx=50, pady=50)

def button_clicked():
    prompt = input.get()
    kilometers = round((float(prompt) * 1.609),2)
    result.config(text=kilometers,font=('Arial',12,'normal'))

#text input
input = Entry(width=10)

input.get() #gets the string in the input
input.grid(column=1, row=0)

#create label
miles = Label(text='Miles',font=('Arial',12,'normal'))
miles.grid(column=2, row=0)
miles.config(padx=10,pady=5)

is_equal_to = Label(text='is equal to',font=('Arial',12,'normal'))
is_equal_to.grid(column=0, row=1)
is_equal_to.config(padx=10,pady=5)

result = Label(text='0',font=('Arial',12,'normal'))
result.grid(column=1, row=1)

km = Label(text='Km',font=('Arial',12,'normal'))
km.grid(column=2, row=1)

#button
my_button = Button(text='Calculate', command=button_clicked)
my_button.grid(column=1, row=2)






window.mainloop()



