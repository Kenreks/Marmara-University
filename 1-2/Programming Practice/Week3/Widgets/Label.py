from Tkinter import *
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.initUI()

    def initUI(self):
        var = StringVar()
        label = Label(self, textvariable=var)
        var.set("Hey!? How are you doing?")
        label.pack()
        self.pack()

def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()