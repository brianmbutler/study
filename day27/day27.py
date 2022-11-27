from tkinter import *

window = Tk()
window.title('First GUI program')
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

def button_clicked():
    text_input = input.get()
    my_label.config(text=text_input)

  
#create label
my_label = Label(text='I am a label',font=('Arial',24,'bold'))
#must call pack, place, or grid to get it to display
#my_label.pack()
my_label["text"] = "New Text"
#my_label.place(x=0, y=0)  #specific placement in x,y
my_label.grid(column=0, row=0) #place in first column, first row
my_label.config(padx=10,pady=10)

#button
my_button = Button(text='Click me', command=button_clicked)
my_button.grid(column=1, row=1)

my_button2 = Button(text='Click me', command=button_clicked)
my_button2.grid(column=2, row=0)


#text input
input = Entry(width=20)
input.get() #gets the string in the input
input.grid(column=3, row=2)




window.mainloop()



