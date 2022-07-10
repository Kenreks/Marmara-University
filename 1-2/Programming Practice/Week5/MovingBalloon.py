from Tkinter import *

class Balloon:
    def __init__(self, x, y, diameter, color):
        self.x = x
        self.y = y
        self.diameter = diameter
        self.color = color

    def draw(self, canvas):
        canvas.create_oval(self.x, self.y, self.x + self.diameter, self.y + self.diameter, fill=self.color)
        canvas.create_line(self.x + self.diameter / 2, self.y + self.diameter, self.x + self.diameter / 2, self.y + 2 * self.diameter)

    def move(self, x, y):
        self.x = x
        self.y = y

    def moveLeft(self):
        self.x -= 5

    def moveRight(self):
        self.x += 5

    def moveUp(self):
        self.y -= 5

    def moveDown(self):
        self.y += 5


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.pack(fill=BOTH, expand=1)

        self.canvas = Canvas(self)

        self.balloon = Balloon(x=10, y=10, diameter=80, color="red")

        self.updateCanvas()

        self.canvas.focus_set()
        self.canvas.bind("<Button-1>", self.onclick)
        self.canvas.bind("<Left>", self.moveLeft)
        self.canvas.bind("<Right>", self.moveRight)
        self.canvas.bind("<Up>", self.moveUp)
        self.canvas.bind("<Down>", self.moveDown)

        self.canvas.pack(fill=BOTH, expand=1)

    def updateCanvas(self):
        self.canvas.delete(ALL)
        self.balloon.draw(self.canvas)

    def onclick(self, event):
        self.balloon.move(event.x, event.y)
        self.updateCanvas()

    def moveLeft(self, event):
        self.balloon.moveLeft()
        self.updateCanvas()

    def moveRight(self, event):
        self.balloon.moveRight()
        self.updateCanvas()

    def moveUp(self, event):
        self.balloon.moveUp()
        self.updateCanvas()

    def moveDown(self, event):
        self.balloon.moveDown()
        self.updateCanvas()


def main():
    root = Tk()
    root.geometry("400x300+300+300")
    app = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()

