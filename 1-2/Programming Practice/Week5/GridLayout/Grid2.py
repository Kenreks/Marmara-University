from Tkinter import *
root = Tk()
colours = ['red','green','orange','white','yellow','blue']
r = 0

Grid.columnconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 1, weight=1)
for c in colours:
    Label(root, text=c).grid(row=r,column=0, sticky=E)
    Entry(root, bg=c).grid(row=r,column=1, sticky=N+S+E+W)
    Grid.rowconfigure(root, r, weight = 1)
    r = r + 1


root.mainloop()
