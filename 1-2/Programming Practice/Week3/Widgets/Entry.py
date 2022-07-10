from Tkinter import *
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.pack()
        L1 = Label(self, text="User Name")
        L1.pack()
        E1 = Entry(self)
        E1.pack()

def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()