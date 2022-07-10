from Tkinter import *

root = Tk()


colors = ['red', 'yellow', 'green']
color_index = 0

def onClick(event):
    global color_index
    widget = event.widget
    color_index = (color_index+1) % len(colors)
    widget.config(bg = colors[color_index])
    print "clicked at", event.x, event.y

frame = Frame(root, width=100, height=100)
label = Label(frame, text = 'Click me to change my color!')
label.bind("<Button-3>", onClick)
label.pack()
frame.pack()

root.mainloop()