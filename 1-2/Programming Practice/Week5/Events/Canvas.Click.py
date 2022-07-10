from Tkinter import *

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.initUI()

    def initUI(self):
        canvas = Canvas(self)
        canvas.bind("<Button-1>", self.onLeftClick)
        canvas.bind("<Button-2>", self.onRightClick)
        # layout
        canvas.pack(fill=BOTH, expand = True)
        self.pack()

    def onLeftClick(self, event):
        self.onClick(event, 'red')

    def onRightClick(self, event):
        self.onClick(event, 'green')

    def onClick(self, event, color):
        print "hi there, everyone!"
        canvas = event.widget
        canvas.create_oval(event.x, event.y, event.x + 10, event.y + 10, fill=color)

def main():
    root = Tk()
    root.title('Hello Button!')
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()

main()

