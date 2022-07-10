from tkinter import *
class calculator(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.buttons()
    def buttons(self):
        self.var = StringVar()
        self.user_input_entry = Entry(self,textvariable = self.var,width=50)
        self.user_input_entry.grid(row=0, columnspan=4, sticky=EW)
        self.button1 = Button(self,text = 1,relief = GROOVE)
        self.button2 = Button(self,text = 2,relief = GROOVE)
        self.button3 = Button(self, text=3, relief=GROOVE)
        self.button4 = Button(self, text=4, relief=GROOVE)
        self.button5 = Button(self, text=5, relief=GROOVE)
        self.button6 = Button(self, text=6, relief=GROOVE)
        self.button7 = Button(self, text=7, relief=GROOVE)
        self.button8 = Button(self, text=8, relief=GROOVE)
        self.button9 = Button(self, text=9, relief=GROOVE)
        self.button0 = Button(self, text=0, relief=GROOVE)
        self.button_add = Button(self,text = "+",relief = GROOVE)
        self.button_sub = Button(self,text = "-",relief = GROOVE)
        self.button_mult = Button(self,text = "*",relief = GROOVE)
        self.button_div = Button(self,text = "/",relief = GROOVE)
        self.button_cls = Button(self,text = "Cls",relief = GROOVE)
        self.button_back = Button(self,text ="Back",relief = GROOVE)
        self.button_close = Button(self,text ="Close",relief = GROOVE)
        self.button_empty = Button(self,text = "",relief = GROOVE)
        self.button_dot = Button(self,text = ".",relief = GROOVE)
        self.button_equal = Button(self,text = "=",relief = GROOVE)

        ButtonsList = [self.button_cls,self.button_back,self.button_empty,self.button_close,self.button7,self.button8,self.button9
                       ,self.button_div,self.button4,self.button5,self.button6,self.button_mult,self.button1,self.button2,self.button3
            ,self.button_sub,self.button0,self.button_dot, self.button_equal, self.button_add]
        row = 1
        column = 0
        for button in ButtonsList:
            button.grid(row = row, column = column , sticky =EW)
            button.bind("<ButtonRelease-1>",self.Calculation)
            column += 1
            if column == 4:
                row += 1
                column = 0

        self.grid()
    def Calculation(self,event):
        if event.widget["text"] == "Cls":
            self.user_input_entry.delete(0, "end")
        elif event.widget["text"] == "Back":
            self.user_input_entry.delete(len(self.user_input_entry.get()) - 1)
        elif event.widget["text"] == "Close":
            exit()
        elif event.widget["text"]=="=":
            self.value = eval(self.user_input_entry.get()+".0")
            self.var =  self.value
            self.user_input_entry.delete(0, "end")
            self.user_input_entry.insert(END, self.var)
        else:
            self.user_input_entry.insert(END,str(event.widget["text"]))
def main():
    root = Tk()
    Cal = calculator(root)
    root.title("Calculator")
    root.mainloop()
main()