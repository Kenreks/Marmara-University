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

        Label(self, bg="red").grid(row=0, column=0, sticky=("N", "S", "E", "W"))
        Label(self, bg="blue").grid(row=1, column=0, sticky=("N", "S", "E", "W"))
        Label(self, bg="green").grid(row=0, column=1, sticky=("N", "S", "E", "W"))
        Label(self, bg="yellow").grid(row=1, column=1, sticky=("N", "S", "E", "W"))

def main():
    root = Tk()
    root.geometry("400x300+300+300")
    app = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()
