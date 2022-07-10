from Tkinter import *
import random
class Color(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.initUI()
        self.Stop = False

    def initUI(self):
        # Widgets
        self.var = StringVar()
        self.var.set('empty')

        self.fast = Checkbutton(text = "Fast",variable = self.var,onvalue='fast')
        self.normal = Checkbutton(text = "Normal",variable = self.var,onvalue = 'normal')
        self.slow = Checkbutton(text = "Slow",variable = self.var,onvalue ='slow')
        self.start = Button(text = "START",command = self.initialfunc)
        self.stop = Button(text = "STOP ",command = self.stopFunction)
        self.your_color = Button(text = "Your Color", width = 15)
        self.score = Button(text = "Score", width = 10)
        self.button1 = Button(text = "Button 1", height = 5, width = 15,command = self.button1_control)
        self.button2 = Button(text = "Button 2", height = 5, width = 15,command = self.button2_control)
        self.button3 = Button(text = "Button 3", height = 5, width = 15,command = self.button3_control)

        #Packing
        self.fast.pack()
        self.normal.pack()
        self.slow.pack()
        self.start.pack()
        self.stop.pack()
        self.your_color.pack()
        self.score.pack()
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()

    def initialfunc(self):
        # only work once
        self.new_score = 0 # initially
        self.colors =['red','green','blue']
        self.selected_color = random.choice(self.colors)
        self.your_color.configure(bg=self.selected_color)

        chosen = self.var.get() # gets the value from the string var

        if chosen == 'fast':
            self.speed = 500
        elif chosen == 'normal':
            self.speed = 1000
        elif chosen == 'slow':
            self.speed = 2000
        self.Stop = False

        self.start_fun()

    def start_fun(self):
        # run evey x sec
        if self.Stop == True:
            return
        # 3 random colors, 3 random number to place them into the big buttons
        random_colors = [random.choice(self.colors),random.choice(self.colors),random.choice(self.colors)]

        random_numbers = [random.randint(1,100),random.randint(1,100),random.randint(1,100)]

        max_list = [0] # to prevent the error from the max function
        for number,color in zip(random_numbers,random_colors):
            if color == self.selected_color:
                max_list.append(number)

        self.max = max(max_list)

        self.button1.configure(text=random_numbers[0],bg=random_colors[0])
        self.button2.configure(text=random_numbers[1],bg=random_colors[1])
        self.button3.configure(text=random_numbers[2],bg=random_colors[2])

        self.rerunning = self.after(self.speed,self.start_fun)

    def button1_control(self):
        button_text = self.button1.cget('text')
        button_color = self.button1.cget('bg') # go the object and get me the bg value

        if button_text == self.max and button_color == self.selected_color:
            self.new_score += 10
            self.score.configure(text="Score: "+str(self.new_score))
        else:
            self.new_score -= 5
            self.score.configure(text="Score: "+str(self.new_score))


    def button2_control(self):
        button_text = self.button2.cget('text')
        button_color = self.button2.cget('bg') # go the object and get me the bg value

        if button_text == self.max and button_color == self.selected_color:
            self.new_score += 10
            self.score.configure(text="Score: " + str(self.new_score))
        else:
            self.new_score -= 5
            self.score.configure(text="Score: " + str(self.new_score))

    def button3_control(self):
        button_text = self.button3.cget('text')
        button_color = self.button3.cget('bg') # go the object and get me the bg value

        if button_text == self.max and button_color == self.selected_color:
            self.new_score += 10
            self.score.configure(text="Score: " + str(self.new_score))
        else:
            self.new_score -= 5
            self.score.configure(text="Score: " + str(self.new_score))

    def stopFunction(self):
        self.Stop = True






def main():
    root = Tk()
    app = Color(root)
    root.geometry("300x500+150+120")
    root.title("Color Game")
    root.mainloop()
main()
