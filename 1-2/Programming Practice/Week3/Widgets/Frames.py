
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
        frame1.pack(side=LEFT, padx=30)

        # frame 2
        frame2 = Frame(self, borderwidth=2, relief=GROOVE, height=400)
        frame2.config(width=400)
        frame2.pack(side=LEFT, fill = BOTH, expand = True, padx=10, pady=50)

        # frame 3
        frame3 = Frame(frame1, borderwidth=2, relief=GROOVE)
        frame3.pack(side=LEFT, padx=5, pady=5)

        # Adjust the labels
        Label(frame1, text="Frame 1").pack(padx=10, pady=10)
        Label(frame2, text="Frame 2").pack(padx=10, pady=10)
        Label(frame3, text="Frame 3").pack(padx=10, pady=10)


def main():
    root = Tk()
    root.geometry("350x150+300+300")
    app = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()