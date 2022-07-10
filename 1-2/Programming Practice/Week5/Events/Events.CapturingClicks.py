from Tkinter import *

root = Tk()

def onClick(event):
    print "clicked at", event.x, event.y

frame = Frame(root, bg="yellow", width=100, height=100)
frame.bind("<Button-1>", onClick)
frame.pack(fill=BOTH, expand=True)

root.mainloop()