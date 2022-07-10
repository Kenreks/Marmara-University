from tkinter import *
import random

class ColorGame(Frame):
    def __init__(self, parent):
        self.parent = parent
        Frame.__init__(self, parent)
        self.initUI(parent)
        self.colors_list = ['red', 'green', 'blue']
        self.user_score = 0
        self.stop = False

    def initUI(self, parent):
        self.var = StringVar()
        self.var.set('e')

        self.fast_button = Checkbutton(self, text = 'Fast', variable = self.var, onvalue = 'Fast')
        self.fast_button.pack()

        self.normal_button = Checkbutton(self, text = 'Normal', variable = self.var, onvalue = 'Normal')
        self.normal_button.pack()

        self.slow_button = Checkbutton(self, text = 'Slow', variable = self.var, onvalue = 'Slow')
        self.slow_button.pack()

        self.start_button = Button(self, text = 'START', width = 5, command = self.game_start)
        self.start_button.pack()

        self.stop_button = Button(self, text = 'STOP', width = 5, command = self.stop_function)
        self.stop_button.pack()

        self.user_color_button = Button(self, text = 'Your Color', width = 20, height =2)
        self.user_color_button.pack()

        self.score_button = Button(self, text = 'Score: ', width = 10)
        self.score_button.pack()

        self.box_1 = Button(self, text ='Button 1', width = 20, height = 5, command = self.getValue_Color1)
        self.box_1.pack()

        self.box_2 = Button(self, text = 'Button 2',width = 20, height = 5, command = self.getValue_Color2)
        self.box_2.pack()

        self.box_3 = Button(self, text = 'Button 3', width = 20, height =5, command = self.getValue_Color3)
        self.box_3.pack()
        self.pack()

    def game_start(self):
        speed = self.var.get()
        if speed == 'Fast':
            self.speed= 500
        if speed == 'Normal':
            self.speed = 1000
        if speed == 'Slow':
            self.speed = 2000
        self.user_color = random.choice(self.colors_list)
        self.user_color_button.configure(bg = self.user_color)
        self.stop = False
        self.game_main()

    def game_main(self):
        if self.stop:
            return
        scor_list = [random.randint(1,100), random.randint(1,100),random.randint(1,100)]
        colors_list = [random.choice(self.colors_list), random.choice(self.colors_list), random.choice(self.colors_list)]
        max_list = [0]
        order = 0
        for color in colors_list:
            if color == self.user_color:
                max_list.append(scor_list[order])
            order +=1
        self.max = max(max_list)
        self.box_1.configure(bg=colors_list[0], text = scor_list[0],font = ('','12','bold'))
        self.box_2.configure(bg=colors_list[1], text = scor_list[1], font = ('','12','bold'))
        self.box_3.configure(bg=colors_list[2], text = scor_list[2], font = ('','12','bold'))
        self.update_idletasks()

        self.updating=self.after(self.speed, self.game_main)

    def getValue_Color1(self):
        if self.box_1.cget('text') == self.max and self.box_1.cget('bg') == self.user_color:
            self.user_score += 10
        else:
            self.user_score -= 5
        self.score_button.configure(text = 'Score: ' + str(self.user_score))

    def getValue_Color2(self):
        if self.box_2.cget('text') == self.max and self.box_2.cget('bg') == self.user_color:
            self.user_score += 10
        else:
            self.user_score -= 5
        self.score_button.configure(text = 'Score: ' + str(self.user_score))

    def getValue_Color3(self):
        if self.box_3.cget('text') == self.max and self.box_3.cget('bg') == self.user_color:
            self.user_score += 10
        else:
            self.user_score -= 5
        self.score_button.configure(text = 'Score: ' + str(self.user_score))
    def stop_function(self):
        self.stop = True

def main():
    root = Tk()
    root.title('Color Game')
    root.geometry('800x600')
    app = ColorGame(root)
    root.mainloop()


main()