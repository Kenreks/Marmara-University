
from Tkinter import *
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.pack()
        acts = ['Maltepe', 'Uskudar',
                'Kadikoy', 'Kartal']

        lb = Listbox(self, selectmode='multiple')
        for i in acts:
            lb.insert(END, i)


        lb.pack(pady=40)

def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()