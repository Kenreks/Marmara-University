from Tkinter import Tk, Frame, Checkbutton
from Tkinter import BooleanVar, BOTH


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.initUI()


    def initUI(self):

        self.parent.title("Checkbutton")

        self.pack(fill=BOTH, expand=True)
        self.var = BooleanVar()

        cb = Checkbutton(self, text="Show title",
            variable=self.var, command=self.onClick)
        cb.select()
        cb.place(x=50, y=50)


    def onClick(self):

        if self.var.get() == True:
            self.parent.title("Checkbutton")
        else:
            self.parent.title("")


def main():

    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()