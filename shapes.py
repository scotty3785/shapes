from tkinter import Tk, Canvas, BOTH
from random import randint, choice

class Paper(Tk):

    def __init__(self, width=600, height=600):
        try:
            super().__init__()
        except:
            print("Could not instantiate Paper")
            
        self.title( "Drawing shapes" )
        self.geometry(str(width)+"x"+str(height))
        self.paper_width = width
        self.paper_height = height
    
        # Create a tkinter canvas object
        self.canvas = Canvas(self)
        self.canvas.pack(fill=BOTH, expand=1)


class Shape():

    # Static variable removing the need to pass a Paper object
    paper = Paper()

    def __init__(self, width=50, height=50, x=None, y=None, color="black"):
        self.height = height
        self.width = width
        self.color = color
        #self.paper = paper
        # Put it in the centre if no coords were given
        if x is None:
            self.x = (self.paper.paper_width/2) - (self.width/2)
        else:
            self.x = x
        if y is None:
            self.y = (self.paper.paper_height/2) - (self.height/2)
        else:
            self.y = y

    # This is an internal method not meant to be used
    def _location(self):
        x1 = self.x
        y1 = self.y 
        x2 = self.x + self.width
        y2 = self.y + self.height
        return [x1, y1, x2, y2]
        
    # Randomly generate what it looks like
    def randomise(self, width=20, height=200):

        self.width = randint(width, height)
        self.height = randint(width, height)

        self.x = randint(0, self.paper.paper_width-self.width)
        self.y = randint(0, self.paper.paper_height-self.height)

        self.color = choice(["red", "yellow", "blue", "green", "gray", "white", "black", "cyan"])

    def set_width(self, width):
        self.width = width

    def set_height(self,height):
        self.height = height

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_color(self, color):
        self.color = color


class Rectangle(Shape):

    def draw(self):
        x1, y1, x2, y2 = self._location()

        # Draw the rectangle
        self.paper.canvas.create_rectangle(x1, y1, x2, y2, fill=self.color)


class Oval(Shape):

    def draw(self):
        x1, y1, x2, y2 = self._location()

        # Draw the oval
        self.paper.canvas.create_oval(x1, y1, x2, y2, fill=self.color)


class Triangle(Shape):

    def __init__(self, x1=0, y1=0, x2=20, y2=0, x3=20, y3=20, color="black"):

        try:
            super().__init__(color=color)
        except:
            print("Could not instantiate Triangle")

        # Remove height and width attributes which make no sense for a triangle
        del self.height
        del self.width

        # Instead add three coordinate attributes
        self.x = x1
        self.y = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def _location(self):
        return [self.x, self.y, self.x2, self.y2, self.x3, self.y3]

    def draw(self):
        x1, y1, x2, y2, x3, y3 = self._location()
        # Draw a triangle
        self.paper.canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill=self.color)

    def randomise(self):
        # Randomise all the points of the triangle
        self.x = randint(0, self.paper.paper_width)
        self.y = randint(0, self.paper.paper_height)
        self.x2 = randint(0, self.paper.paper_width)
        self.y2 = randint(0, self.paper.paper_height)
        self.x3 = randint(0, self.paper.paper_width)
        self.y3 = randint(0, self.paper.paper_height)

        self.color = choice(["red", "yellow", "blue", "green", "gray", "white", "black", "cyan"])

    def set_width(self, width):
        print("Width is not defined for Triangle objects")

    def set_height(self, height):
        print("Height is not defined for Triangle objects")
        


# If you run this file it will auto do this demo script
if __name__ == "__main__":

    # Random size and location triangle
    tri = Triangle()
    tri.randomise()
    tri.draw()

    # Specific size and location rectangle
    rect = Rectangle(height=40, width=90, x=110, y=20, color="yellow")
    rect.draw()

    # Default oval
    oval = Oval()
    oval.draw()

    # Oval with setters
    oval2 = Oval()
    oval2.set_height(200)
    oval2.set_width(100)
    oval2.set_color("fuchsia")
    oval2.set_x(30)
    oval2.set_y(90)
    oval2.draw()
