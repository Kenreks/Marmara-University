from Tkinter import Tk, W, E, StringVar, RIGHT, X, LEFT
from ttk import Frame, Button, Style
from ttk import Entry, Label


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        Style().configure("TButton", padding=(0, 5, 0, 5), width=8, font='serif 10')

        self.screenvar = StringVar()
        self.screenstr = ''
        self.screen = Label(self, textvariable=self.screenvar, justify=RIGHT)
        self.cls = Button(text="Cls", command=self.clsButtonEvent)
        self.bck = Button(text="Back", command=self.backButtonEvent)
        self.lbl = Button()
        self.clo = Button(text="Close", command=self.closeButtonEvent)
        self.sev = Button(text="7", command=self.number7ButtonEvent)
        self.eig = Button(text="8", command=self.number8ButtonEvent)
        self.nin = Button(text="9", command=self.number9ButtonEvent)
        self.div = Button(text="/", command=self.divButtonEvent)

        self.fou = Button(text="4", command=self.number4ButtonEvent)
        self.fiv = Button(text="5", command=self.number5ButtonEvent)
        self.six = Button(text="6", command=self.number6ButtonEvent)
        self.mul = Button(text="*", command=self.mulButtonEvent)
        
        self.one = Button(text="1", command=self.number1ButtonEvent)
        self.two = Button(text="2", command=self.number2ButtonEvent)
        self.thr = Button(text="3", command=self.number3ButtonEvent)
        self.mns = Button(text="-", command=self.minButtonEvent)

        self.zer = Button(text="0", command=self.number0ButtonEvent)
        self.dot = Button(text=".", command=self.dotButtonEvent)
        self.equ = Button(text="=", command=self.eqButtonEvent)
        self.pls = Button(text="+", command=self.plusButtonEvent)

        # self.UIWithPack() # Pack Layout
        self.UIWithGrid()  # Grid Layout
        self.pack()

    def UIWithPack(self):
        frame1 = Frame(self)
        frame2 = Frame(self)
        frame3 = Frame(self)
        frame4 = Frame(self)
        frame5 = Frame(self)

        self.screen.pack(fill=X)
        for frame in(frame1, frame2, frame3, frame4, frame5):
            frame.pack()

        for widget_1 in (self.cls, self.bck, self.lbl, self.clo):
            widget_1.pack(in_=frame1, side=LEFT)

        for widget_1 in (self.sev, self.eig, self.nin, self.div):
            widget_1.pack(in_=frame2, side=LEFT)

        for widget_1 in (self.fou, self.fiv, self.six, self.mul):
            widget_1.pack(in_=frame3, side=LEFT)

        for widget_1 in (self.one, self.two, self.thr, self.mns):
            widget_1.pack(in_=frame4, side=LEFT)

        for widget_1 in (self.zer, self.dot, self.equ, self.pls):
            widget_1.pack(in_=frame5, side=LEFT)

    def UIWithGrid(self):
        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)

        self.screen.grid(row=0, columnspan=4, sticky=W+E)
        self.cls.grid(in_=self, row=1, column=0)
        self.bck.grid(in_=self, row=1, column=1)
        self.lbl.grid(in_=self, row=1, column=2)
        self.clo.grid(in_=self, row=1, column=3)

        self.sev.grid(in_=self, row=2, column=0)
        self.eig.grid(in_=self, row=2, column=1)
        self.nin.grid(in_=self, row=2, column=2)
        self.div.grid(in_=self, row=2, column=3)

        self.fou.grid(in_=self, row=3, column=0)
        self.fiv.grid(in_=self, row=3, column=1)
        self.six.grid(in_=self, row=3, column=2)
        self.mul.grid(in_=self, row=3, column=3)

        self.one.grid(in_=self, row=4, column=0)
        self.two.grid(in_=self, row=4, column=1)
        self.thr.grid(in_=self, row=4, column=2)
        self.mns.grid(in_=self, row=4, column=3)

        self.zer.grid(in_=self, row=5, column=0)
        self.dot.grid(in_=self, row=5, column=1)
        self.equ.grid(in_=self, row=5, column=2)
        self.pls.grid(in_=self, row=5, column=3)

    def number1ButtonEvent(self):
        self.screenstr += '1'
        self.screenvar.set(self.screenstr)

    def number2ButtonEvent(self):
        self.screenstr += '2'
        self.screenvar.set(self.screenstr)

    def number3ButtonEvent(self):
        self.screenstr += '3'
        self.screenvar.set(self.screenstr)

    def number4ButtonEvent(self):
        self.screenstr += '4'
        self.screenvar.set(self.screenstr)

    def number5ButtonEvent(self):
        self.screenstr += '5'
        self.screenvar.set(self.screenstr)

    def number6ButtonEvent(self):
        self.screenstr += '6'
        self.screenvar.set(self.screenstr)

    def number7ButtonEvent(self):
        self.screenstr += '7'
        self.screenvar.set(self.screenstr)

    def number8ButtonEvent(self):
        self.screenstr += '8'
        self.screenvar.set(self.screenstr)

    def number9ButtonEvent(self):
        self.screenstr += '9'
        self.screenvar.set(self.screenstr)

    def number0ButtonEvent(self):
        self.screenstr += '0'
        self.screenvar.set(self.screenstr)

    def divButtonEvent(self):
        self.screenstr += '/'
        self.screenvar.set(self.screenstr)

    def mulButtonEvent(self):
        self.screenstr += '*'
        self.screenvar.set(self.screenstr)

    def minButtonEvent(self):
        self.screenstr += '-'
        self.screenvar.set(self.screenstr)

    def plusButtonEvent(self):
        self.screenstr += '+'
        self.screenvar.set(self.screenstr)

    def closeButtonEvent(self):
        self.parent.destroy()

    def backButtonEvent(self):
        self.screenstr = self.screenstr[:-1]
        self.screenvar.set(self.screenstr)

    def dotButtonEvent(self):
        self.screenstr += '.'
        self.screenvar.set(self.screenstr)

    def eqButtonEvent(self):
        self.screenstr = str(eval(self.screenstr))
        self.screenvar.set(self.screenstr)

    def clsButtonEvent(self):
        self.screenstr = ''
        self.screenvar.set(self.screenstr)


def main():
    root = Tk()
    root.title("Calculator")
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()