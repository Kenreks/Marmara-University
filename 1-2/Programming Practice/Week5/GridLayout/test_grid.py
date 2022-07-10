__author__ = 'acakmak'
from Tkinter import *
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.pack()

        # frame 1
        frame1 = Frame(self, borderwidth=2, relief=GROOVE)
        frame1.grid(row=0, column=0)

        # frame 2
        frame2 = Frame(self, borderwidth=2, relief=GROOVE)
        frame2.grid(row=1, column=0, sticky=EW)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=3)

        self.columnconfigure(0, weight=2)

        # Adjust the labels
        Label(frame1, text="Frame 1", bg='yellow').pack(fill=BOTH, expand=True)
        Label(frame2, text="Frame 2", bg='red').pack(fill=BOTH, expand=True)





def main():
    root = Tk()
    root.geometry("350x150+300+300")
    app = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()