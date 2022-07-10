from Tkinter import *

root = Tk()

colours = ['red','green']

r = 0
for c in colours:
    Label(root, text=c).grid(row=r,column=0, sticky=EW)
    Entry(root, bg=c).grid(row=r,column=1)
    r = r + 1

root.mainloop()
