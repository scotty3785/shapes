from guizero import App, PushButton
from shapes import Triangle, Rectangle, Oval, Paper

def changeMe():
    w = r.width
    h = r.height
    r.width = w+20
    r.height = h+20


app = App(width=600,height=600)
button = PushButton(app, changeMe, text = "Click me")



p = Paper(app)
t = Triangle(p)
t.randomize()
t.draw()

t2 = Triangle(p)
t2.randomize()
t2.draw()

r = Rectangle(p)
r.randomize()
r.width = 400

r.draw()
r.color ='red'
r.width = 20

app.display()

#p = Paper()
#p.mainloop()

#tri = Triangle()
#tri.randomize()
#tri.draw()


