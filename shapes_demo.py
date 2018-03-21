from guizero import App, PushButton
from shapes import Triangle, Rectangle, Oval, Paper

def changeMe():
    w = r.get_width()
    h = r.get_height()
    r.set_width(w+20)
    r.set_height(h+20)


app = App()
button = PushButton(app, changeMe, text = "Click me")



p = Paper(app.tk)
t = Triangle(p)
t.randomize()
t.draw()

t2 = Triangle(p)
t2.randomize()
t2.draw()

r = Rectangle(p)
r.randomize()
r.set_width(400)

r.draw()
r.set_color('red')
r.set_width(20)

app.display()

#p = Paper()
#p.mainloop()

#tri = Triangle()
#tri.randomize()
#tri.draw()


