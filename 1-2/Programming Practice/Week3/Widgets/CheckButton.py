
from Tkinter import *

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.pack()
        self.var = BooleanVar()
        self.var.set(False)
        self.onClick()
        cb = Checkbutton(self, text="Show title: ",
            variable=self.var, command=self.onClick)
        cb.pack()

    def onClick(self):
        if self.var.get() == True:
            self.parent.title("Hello Checkbutton!")
        else:
            self.parent.title("")

def main():
    root = Tk()
    root.geometry("250x150+300+300")
    root.title('Hello Checkbutton!')
    app = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()