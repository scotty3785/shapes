# This code requires Python 3 and tkinter (which is usually installed by default)
# This code will NOT work on trinket.io as the tkinter module is not supported
# Raspberry Pi Foundation 2017
# CC-BY-SA 4.0

try:
    from guizero import App
    from tkinter import *
except ImportError:
    print("guizero or tkinter did not import successfully - check you are running Python 3 and that guizero/tkinter is available.")
    exit(1)

import random

class Paper():

    def __init__(self, master,  width=300, height=300):

        """Create a Paper object which allows shapes to be drawn onto it.
        """

        # Call the constructor from the superclass (tkinter's Tk)
        #try:
            #super().__init__()
        #except ValueError:
            #print("Error: could not instantiate Paper object")

        # Set some attributes
        #self.title( "Drawing shapes" )
        #self.geometry(str(width)+"x"+str(height))
        self.paper_width = width
        self.paper_height = height

        # Create a tkinter canvas object to draw on
        self.canvas = Canvas(master.tk)
        self.canvas.pack(fill=BOTH, expand=1)
        
    def set_background(self,color):
        self.canvas['bg'] = color


class Shape():

    # Static class variable removing the need to pass in a Paper object
    # to draw the shapes on
    #paper = Paper()

    # Constructor for Shape
    def __init__(self, paper, width=50, height=50, x=None, y=None, color="black"):
        self.paper = paper
        """Creates a generic 'shape' which contains properties common to all
        shapes such as height, width, x y coordinates and colour.
        """

        # Set some attributes
        self._height = height
        self._width = width
        self._color = color

        # Put the shape in the centre if no xy coords were given
        if x is None:
            self._x = (self.paper.paper_width/2) - (self._width/2)
        else:
            self._x = x
        if y is None:
            self._y = (self.paper.paper_height/2) - (self._height/2)
        else:
            self._y = y

    # This is an internal method not meant to be called by users
    # (It has a _ before the method name to show this)
    def _location(self):
        """Internal method used by the class to get the location
        of the shape. This shouldn't be called by users, hence why its
        name begins with an underscore.
        """

        x1 = self._x
        y1 = self._y
        x2 = self.x + self._width
        y2 = self.y + self._height
        return (x1, y1, x2, y2)

    # Randomly generate what the shape looks like
    def randomize(self, smallest=20, largest=200):

        """Randomly generates width, height, position and colour for a shape. You can specify
        the smallest and largest random size that will be generated. If not specified, the
        generated shape will default to a random size between 20 and 200.
        """

        self.width = random.randint(smallest, largest)
        self.height = random.randint(smallest, largest)

        self.x = random.randint(0, self.paper.paper_width-self._width)
        self.y = random.randint(0, self.paper.paper_height-self._height)

        self.color = random.choice(["red", "yellow", "blue", "green", "gray", "white", "black", "cyan", "pink", "purple"])

    def _redraw(self):
        """Internal method to change the location of an existing shape"""
        if hasattr(self,'shapeObj'):
            #x1,y1,x2,y2 = self._location()
            location = self._location()
            #self.paper.canvas.coords(self.shapeObj,x1,y1,x2,y2)
            self.paper.canvas.coords(self.shapeObj,location)

    def move(self,dx,dy):
        self._x += dx
        self._y += dy
        self._redraw()
    
    # Getters and setters for Shape attributes
    @property    
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width):
        """Sets the width of the shape"""
        self._width = width
        self._redraw()

    @property        
    def height(self):
        return self._height

    @height.setter
    def height(self,height):
        """Sets the height of the shape"""
        self._height = height
        self._redraw()

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x position of the shape"""
        self._x = x
        self._redraw()

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y position of the shape"""
        self._y = y
        self._redraw()

    @property
    def color(self):
        """Returns the colour of the shape"""
        return self._color

    @color.setter
    def color(self, color):
        """Sets the colour of the shape"""
        self._color = color
        if hasattr(self,'shapeObj'):
            self.paper.canvas.itemconfig(self.shapeObj,fill=self._color)
            



# Rectangle class is a subclass of Shape
class Rectangle(Shape):

    # This is how to draw a rectangle
    def draw(self):

        """Draws a rectangle on the canvas. The properties of the rectangle
        can be set using the getter and setter methods in Shape"""

        x1, y1, x2, y2 = self._location()

        # Draw the rectangle
        self.shapeObj = self.paper.canvas.create_rectangle(x1, y1, x2, y2, fill=self._color)


class Oval(Shape):

    def draw(self):

        """Draws an oval on the canvas. The properties of the oval
        can be set using the getter and setter methods in Shape"""

        x1, y1, x2, y2 = self._location()

        # Draw the oval
        self.shapeObj = self.paper.canvas.create_oval(x1, y1, x2, y2, fill=self._color)


class Triangle(Shape):

    # Every constructor parameter has a default setting
    # e.g. color defaults to "black" but you can override this
    def __init__(self, paper, x1=0, y1=0, x2=20, y2=0, x3=20, y3=20, color="black"):
        self.paper = paper
        """Overrides the Shape constructor because triangles require three
        coordinate points to be drawn, unlike rectangles and ovals."""

        try:
            super().__init__(self.paper, color=color)
        except ValueError:
            print("Error: could not instantiate Triangle")

        # Remove height and width attributes which make no sense for a triangle
        # (triangles are drawn via 3 xy coordinates)
        del self._height
        del self._width

        # Instead add three coordinate attributes
        self._x = x1
        self._y = y1
        self._x2 = x2
        self._y2 = y2
        self._x3 = x3
        self._y3 = y3

    def _location(self):

        """Internal method used by the class to get the location
        of the triangle. This shouldn't be called by users, hence why its
        name begins with an underscore.
        """

        return (self._x, self._y, self._x2, self._y2, self._x3, self._y3)

    def move(self,dx,dy):
        cur_location = self._location()
        new_location = (cur_location[0]+dx,
                        cur_location[1]+dy,
                        cur_location[2]+dx,
                        cur_location[3]+dy,
                        cur_location[4]+dx,
                        cur_location[5]+dy)
        self._x, self._y, self._x2, self._y2, self._x3, self._y3 = new_location
        self._redraw()
        pass

    def draw(self):

        """Draws a triangle on the canvas. The properties of the triangle
        can be set using the getter and setter methods in Shape"""

        x1, y1, x2, y2, x3, y3 = self._location()
        # Draw a triangle
        self.shapeObj = self.paper.canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill=self._color)

    def randomize(self):

        """Randomly chooses the location of all 3 triangle points as well
        as the colour of the triangle"""

        # Randomly choose all the points of the triangle
        self._x = random.randint(0, self.paper.paper_width)
        self._y = random.randint(0, self.paper.paper_height)
        self._x2 = random.randint(0, self.paper.paper_width)
        self._y2 = random.randint(0, self.paper.paper_height)
        self._x3 = random.randint(0, self.paper.paper_width)
        self._y3 = random.randint(0, self.paper.paper_height)

        # Randomly choose a colour of this triangle
        self._color = random.choice(["red", "yellow", "blue", "green", "gray", "white", "black", "cyan", "pink", "purple"])

    # Change the behaviour of set_width and set_height methods for a triangle
    # because triangles are not drawn in the same way
    
    def set_width(self, width):
        """Overrides the setter method for width"""

        print("Width is not defined for Triangle objects")

    def set_height(self, height):
        """Overrides the setter method for height"""

        print("Height is not defined for Triangle objects")


# This if statement means
# "if you run this file (rather than importing it), run this demo script"
if __name__ == "__main__":
    app = App()
    p = Paper(app)
    p.set_background('white')
    
    # Random size and location triangle
    tri = Triangle(p)
    tri.randomize()
    tri.draw()

    # Specific size and location rectangle
    rect = Rectangle(p,height=40, width=90, x=110, y=20, color="yellow")
    rect.draw()

    # Default oval
    oval = Oval(p)
    oval.draw()

    # Oval with setters
    oval2 = Oval(p)
    oval2.height = 200
    oval2.width = 100
    oval2.color = "fuchsia"
    oval2.x = 30
    oval2.y = 90
    oval2.draw()
    
    app.display()
