__author__ = 'acakmak'


from Tkinter import Tk, W, E, StringVar, RIGHT
from ttk import Frame, Button, Style
from ttk import Entry, Label



class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):

        self.parent.title("Calculator")

        Style().configure("TButton", padding=(0, 5, 0, 5),
            font='serif 10')

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)

        self.screenvar = StringVar()
        self.screenstr = ''
        self.screen = Label(self, textvariable=self.screenvar, justify=RIGHT)
        self.screen.grid(row=0, columnspan=4, sticky=W+E)
        cls = Button(self, text="Cls", command=self.clsButtonEvent)
        cls.grid(row=1, column=0)
        bck = Button(self, text="Back", command=self.backButtonEvent)
        bck.grid(row=1, column=1)
        lbl = Button(self)
        lbl.grid(row=1, column=2)
        clo = Button(self, text="Close", command=self.closeButtonEvent)
        clo.grid(row=1, column=3)
        sev = Button(self, text="7", command=self.number7ButtonEvent)
        sev.grid(row=2, column=0)
        eig = Button(self, text="8", command=self.number8ButtonEvent)
        eig.grid(row=2, column=1)
        nin = Button(self, text="9", command=self.number9ButtonEvent)
        nin.grid(row=2, column=2)
        div = Button(self, text="/", command=self.divButtonEvent)
        div.grid(row=2, column=3)

        fou = Button(self, text="4", command=self.number4ButtonEvent)
        fou.grid(row=3, column=0)
        fiv = Button(self, text="5", command=self.number5ButtonEvent)
        fiv.grid(row=3, column=1)
        six = Button(self, text="6", command=self.number6ButtonEvent)
        six.grid(row=3, column=2)
        mul = Button(self, text="*", command=self.mulButtonEvent)
        mul.grid(row=3, column=3)

        one = Button(self, text="1", command=self.number1ButtonEvent)
        one.grid(row=4, column=0)
        two = Button(self, text="2", command=self.number2ButtonEvent)
        two.grid(row=4, column=1)
        thr = Button(self, text="3", command=self.number3ButtonEvent)
        thr.grid(row=4, column=2)
        mns = Button(self, text="-", command=self.minButtonEvent)
        mns.grid(row=4, column=3)

        zer = Button(self, text="0", command=self.number0ButtonEvent)
        zer.grid(row=5, column=0)
        dot = Button(self, text=".", command=self.dotButtonEvent)
        dot.grid(row=5, column=1)
        equ = Button(self, text="=", command=self.eqButtonEvent)
        equ.grid(row=5, column=2)
        pls = Button(self, text="+", command=self.plusButtonEvent)
        pls.grid(row=5, column=3)

        self.pack()

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
    app = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()