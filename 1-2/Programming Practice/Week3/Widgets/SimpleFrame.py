from Tkinter import *

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.initUI()

    def initUI(self):
       self.hi_there = Button(self, text="Hello", command=self.say_hi)
       self.hi_there.pack()
       self.pack()

    def say_hi(self):
        print "hi there, everyone!"



def main():

    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()


main()