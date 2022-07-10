from Tkinter import *

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.pack(fill="both", expand=True)

        Grid.columnconfigure(self, 0, weight=1)
        Grid.columnconfigure(self, 1, weight=1)

        Grid.rowconfigure(self, 0, weight=1)
        Grid.rowconfigure(self, 1, weight=1)

        r = "red"
        b = "blue"
        g = "green"
        y = "yellow"

        Label(self, bg=r).grid(row=0, column=0, sticky=("N", "S", "E", "W"))
        Label(self, bg=b).grid(row=1, column=0, sticky=("N", "S", "E", "W"))
        Label(self, bg=g).grid(row=0, column=1, sticky=("N", "S", "E", "W"))
        Label(self, bg=y).grid(row=1, column=1, sticky=("N", "S", "E", "W"))
        Label.bind("<Button-1>", self.changecolour)
        
    def changecolour(self):
        r = "green"
        g = "blue"
        b = "yellow"
        y = "red"
        self.initUI

def main():
    root = Tk()
    root.geometry("400x300+300+300")
    app = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()
