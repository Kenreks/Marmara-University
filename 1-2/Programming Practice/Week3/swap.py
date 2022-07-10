from Tkinter import *


class HelloApp(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.initUI()

    def initUI(self):
        self.buttonSwap = Button(self)
        self.buttonSwap["command"] = self.clickButton

        self.buttonTextVar = StringVar()
        self.buttonSwap["textvariable"] = self.buttonTextVar

        self.openedVar = BooleanVar()
        checkbuttonOpen =  Checkbutton(self, command=self.clickButton, text="Is Opened?")
        checkbuttonOpen["variable"] = self.openedVar

        self.labelTextVar = StringVar()
        label = Label(self, textvariable=self.labelTextVar)

        self.isOpen = True
        self.updateUI()

        self.buttonSwap.pack()
        checkbuttonOpen.pack()
        label.pack()
        self.pack()

    def updateUI(self):
        if self.isOpen:
            self.close()
        else:
            self.open()


    def open(self):
        self.openedVar.set(True)
        self.buttonTextVar.set("CLOSE")
        self.labelTextVar.set("OPENED")

    def close(self):
        self.openedVar.set(False)
        self.buttonTextVar.set("OPEN")
        self.labelTextVar.set("CLOSED")

    def clickButton(self):
        self.isOpen = not self.isOpen
        self.updateUI()



root = Tk()
root.title("Hello")
root.geometry('250x350+300+300')
HelloApp(root)

root.mainloop()

