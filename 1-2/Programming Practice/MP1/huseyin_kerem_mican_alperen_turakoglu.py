from Tkinter import *
import ttk
import tkFileDialog
import csv
import anydbm
import pickle

class Students():
    def __init__(self, id,name, surname):
        self.name = name
        self.surname = surname
        self.id = id

class StudentsData():
    def __init__(self):
        self.db = anydbm.open("Database.db", 'c')
        return

    def getdata(self,tree,msgvar):
        self.t1 = dict()
        self.t2 = dict()

        import_file_path = tkFileDialog.askopenfilename()
        with open(import_file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                self.t1[str(row[0])] = Students(row[0], row[1], row[2])
                if str(row[1]) in self.t2.keys():
                    self.t2[str(row[1])].append(row[0])
                else:
                    self.t2[str(row[1])] = list()
                    self.t2[str(row[1])].append(row[0])
        self.db["StudentId"] = pickle.dumps(self.t1)
        self.db["Names"] = pickle.dumps(self.t2)

        self.load(tree,msgvar)

    def databaseSearching(self,string,combocurrent,tree,msgvar):
        print string.get(),combocurrent
        self.string = string.get()

        msgvar.set("Program Messages")
        tmp1 = pickle.loads(self.db["StudentId"])
        tmp2 = pickle.loads(self.db["Names"])
        try:
            if combocurrent == 0 :
                for i in tree.get_children():
                    tree.delete(i)
                stdobj = tmp1[self.string]
                tree.insert("","end",text = str(stdobj.id) ,values = (stdobj.name, stdobj.surname ))
            elif combocurrent == 1:
                for i in tree.get_children():
                    tree.delete(i)
                names = tmp2[self.string.capitalize()]
                for i in names :
                    stdobj = tmp1[i]
                    tree.insert("","end",text = str(stdobj.id) , values = (stdobj.name,stdobj.surname))
        except:
            msgvar.set("Can't Found Any Student")
            if self.string == '':
                 self.load(tree,msgvar)
            pass
    def load(self,tree,msgvar):
        self.tree = tree
        for i in tree.get_children():
            tree.delete(i)
        tmp = pickle.loads(self.db["StudentId"])
        for k in tmp:
            self.tree.insert("","end",text=str(tmp[k].id),values=(tmp[k].name, tmp[k].surname))
        if msgvar.get() == "Program Messages...":
            msgvar.set("Students Registered Successfully")

    def update(self,id,name,surname,tree,msgvar):
        self.id = id.get()
        self.name = name.get()
        self.surname = surname.get()
        if self.name == "":
            print "You Should Select A Student Before Updating"
        try:
            tmp1 = pickle.loads(self.db["StudentId"])
            stdobj = tmp1[str(self.id)]
            tmp2 = pickle.loads(self.db["Names"])
            print stdobj.name

            if stdobj.name != self.name:
                tmp2[stdobj.name].remove(str(self.id))
                if self.name in tmp2.keys():
                 tmp2[self.name].append(str(self.id))
                else:
                    tmp2[self.name] = list()
                    tmp2[self.name].append(str(self.id))

            tmp1[str(self.id)].name = self.name
            tmp1[str(self.id)].surname = self.surname
            print tmp2[stdobj.name],tmp2[self.name]
            self.db["StudentId"] = pickle.dumps(tmp1)
            self.db["Names"] = pickle.dumps(tmp2)
            id.set(0)
            name.set("")
            surname.set("")
            msgvar.set("Updated Successfully")
            self.load(tree,msgvar)
        except:
            pass

    def delete(self,id,name,surname,tree,msgvar):
        self.id = id.get()
        self.name = name.get()
        self.surname = surname.get()
        if self.name == "":
            print "You Should Select A Student Before Deleting"
        try :
            tmp1 = pickle.loads(self.db["StudentId"])
            tmp2 = pickle.loads(self.db["Names"])
            stdobj = tmp1[str(self.id)]
            tmp2[stdobj.name].remove(str(self.id))
            del tmp1[str(self.id)]
            self.db["StudentId"] = pickle.dumps(tmp1)
            self.db["Names"] = pickle.dumps(tmp2)
            id.set(0)
            name.set("")
            surname.set("")
            self.load(tree, msgvar)
            msgvar.set("Deleted Successfully")
        except:
            id.set(0)
            name.set("")
            surname.set("")

class GUI(Frame):
    def __init__(self,parent,gateway):
        Frame.__init__(self,parent)
        self.gateway = gateway
        self.parent = parent
        self.fr = Frame(self.parent, bg="#F0F0F0")
        self.fr.pack(fill=X)
        self.idvar = IntVar()
        self.namevar = StringVar()
        self.surnamevar = StringVar()
        self.searchvar = StringVar()
        self.msgvar = StringVar()
        self.msgvar.set("Program Messages...")
        self.initUI()

    def click(self,obj):
        item =  self.tree.identify('item',obj.x,obj.y)
        self.idvar.set(self.tree.item(item)['text'])
        self.namevar.set((pickle.loads(self.gateway.db["StudentId"]))[self.tree.item(item)['text']].name)
        self.surnamevar.set((pickle.loads(self.gateway.db["StudentId"]))[self.tree.item(item)['text']].surname)

    def initUI(self):
        self.title = Label(self.fr, text="Student Registiration Tool", bg="#FF3E96", fg="white", font=("TkDefaultFont", 18, "bold"))
        self.title.pack(fill=X)

        self.Import = Button(self.fr, text="Import New Students", width=20, bd=1,command = lambda : self.gateway.getdata(self.tree,self.msgvar))
        self.Import.pack(pady=10)

        self.lb1 = Label(self.fr,text="Search Student:")
        self.lb1.pack(side=LEFT,anchor=N,padx=5)

        self.Entry = Entry(self.fr,textvariable = self.searchvar)
        self.Entry.pack(side=LEFT,anchor=N,fill=X,expand=Y)

        self.cmb = ttk.Combobox(self.fr,values=["ID","Name"],width=10)
        self.cmb.current(0)
        self.cmb.pack(side=LEFT,anchor=N,padx=5)

        self.searchbt = Button(self.fr,text="Search",width=8,command = lambda : self.gateway.databaseSearching(self.searchvar,self.cmb.current(),self.tree,self.msgvar))
        self.searchbt.pack(side=LEFT,anchor=N,padx=5)
        self.msg = Label(self.parent, textvariable=self.msgvar)
        self.msg.pack(side=BOTTOM, anchor =SW)

        self.tree = ttk.Treeview(self.parent)
        self.tree["columns"]=("one","two")
        self.tree.heading("#0",text="ID",anchor=W)
        self.tree.heading("one",text="Name",anchor=W)
        self.tree.heading("two",text="Surname",anchor=W)
        self.tree.column("#0",width=100)
        self.tree.column("one", width=150)
        self.tree.column("two", width=150)
        self.tree.bind('<Button-1>',self.click)
        self.tree.pack(side=LEFT,fill=BOTH,expand=Y)
        try :
            self.gateway.load(self.tree,self.msgvar)
        except:
            pass

        self.lbfr = LabelFrame(self.parent)
        self.lbfr.pack(side=LEFT,padx=5,pady=5,fill=BOTH,expand=Y)

        self.std = Label(self.lbfr,text="Student Details:",bg="#FF3E96",fg="white")
        self.std.pack(fill=X,anchor=N)

        self.idfr = Frame(self.lbfr)
        self.idfr.pack(fill=X,pady=5)

        self.idlb = Label(self.idfr,text="ID")
        self.idlb.pack(side=LEFT,anchor=NW)

        self.ident = Label(self.idfr,textvariable=self.idvar,bg="#F0F0F0")
        self.ident.pack()

        self.namefr = Frame(self.lbfr)
        self.namefr.pack(fill=X,pady=5)

        self.namelb = Label(self.namefr,text="Name")
        self.namelb.pack(side=LEFT,anchor=NW)

        self.nameent = Entry(self.namefr,textvariable=self.namevar,bd=1)
        self.nameent.pack(anchor=E,padx=5)

        self.surnamefr = Frame(self.lbfr)
        self.surnamefr.pack(fill=X,pady=5)

        self.surnamelb = Label(self.surnamefr,text="Surname")
        self.surnamelb.pack(side=LEFT,anchor=NW)

        self.surnameent = Entry(self.surnamefr,textvariable=self.surnamevar,bd=1)
        self.surnameent.pack(anchor=E,padx=5)

        self.updatebt = Button(self.lbfr, text= "Update User",width=15 ,command = lambda: self.gateway.update(self.idvar,self.namevar,self.surnamevar,self.tree,self.msgvar))
        self.updatebt.pack(pady=10, anchor=S)

        self.deletebt = Button(self.lbfr, text= "Delete User",width=15 ,command = lambda: self.gateway.delete(self.idvar,self.namevar,self.surnamevar,self.tree,self.msgvar))
        self.deletebt.pack(pady=5, anchor=S)

def main():
    gateway = StudentsData()
    root = Tk()
    root.geometry("700x400+700+300")
    root.title("SteelBox Inc. Calculator")
    app = GUI(root,gateway)
    root.mainloop()
if __name__ == '__main__':
    main()