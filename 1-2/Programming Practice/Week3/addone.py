from Tkinter import *
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.pack()

        self.entryVar = StringVar()
        Entry(self, textvariable=self.entryVar).pack()

        Button(self, text="add one", command=self.addOne).pack()

        self.labelVar = StringVar()
        Label(self, textvariable=self.labelVar).pack()

    def addOne(self):
        try:
            intValue = int(self.entryVar.get())
            self.labelVar.set(intValue+1)
        except ValueError:
            self.labelVar.set("invalid input")

def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()