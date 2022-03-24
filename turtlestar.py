import turtle
star = turtle.Turtle()
star.color('red', 'yellow')
star.begin_fill()
while True:
    star.forward(200)
    star.left(170)
    if abs(star.pos()) < 1:
        break
star.end_fill()
star.done()
