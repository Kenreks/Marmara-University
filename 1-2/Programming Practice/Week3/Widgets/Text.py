from Tkinter import *
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.pack()

        button = Button(self, text="insert", command=self.insertByInsert)
        button.pack()

        button = Button(self, text="end", command=self.insertByEnd)
        button.pack()

        self.text = Text(self)
        self.text.insert(INSERT, "Hello.....\n")
        self.text.insert(INSERT, "Bye Bye.....")
        self.text.pack()

        self.text.tag_add("here", "1.0", "1.4") #row 1 column from 0 to 4
        self.text.tag_add("start", "2.2", "2.7") #row 2 column from 2 to 7
        self.text.tag_config("here", background="yellow", foreground="blue")
        self.text.tag_config("start", background="black", foreground="green")

    def insertByInsert(self):
        self.text.insert(INSERT, "++++")

    def insertByEnd(self):
        self.text.insert(END,"++++")

def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()