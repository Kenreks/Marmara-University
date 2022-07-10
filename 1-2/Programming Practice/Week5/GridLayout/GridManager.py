from Tkinter import *

master = Tk()
label1 = Label(master, text="First")
label2 = Label(master, text="Second")
entry1 = Entry(master)
entry2 = Entry(master)
checkbutton = Checkbutton(master, text="Show title")
label3 = Label(master, text='Hello!')
ok_button = Button(master, text="OK")
cancel_button = Button(master, text="Cancel")

label1.grid(sticky=E) # by default column 0 of the next empty row
label2.grid(sticky=E) # can you guess row and column number of this guy?
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
checkbutton.grid(columnspan=2, sticky=W)
label3.grid(row=0, column=2, columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)
ok_button.grid(row=2, column=2)
cancel_button.grid(row=2, column=3)



master.mainloop()