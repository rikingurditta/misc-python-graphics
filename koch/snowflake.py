import turtle as t
from math import sqrt
from numpy import array, matmul

t.hideturtle()
t.color('red')
t.speed(0)

rot60 = array([[0.5, -sqrt(3) / 2], [sqrt(3) / 2, 0.5]])


def draw_koch(p1: array, p2: array, depth: int) -> None:
    diff = p2 - p1
    b1 = p1 + diff / 3
    b2 = p2 - diff / 3
    apex = b1 + matmul(rot60, diff / 3)
    if depth == 0:
        t.penup()
        t.goto(p1[0], p1[1])
        t.pendown()
        t.goto(b1)
        t.goto(apex)
        t.goto(b2)
        t.goto(p2)
    else:
        draw_koch(p1, b1, depth - 1)
        draw_koch(b1, apex, depth - 1)
        draw_koch(apex, b2, depth - 1)
        draw_koch(b2, p2, depth - 1)


DEPTH = 4
SCALE = 256

left = SCALE * array([-1, -sqrt(3) / 3])
apex = SCALE * array([0, sqrt(3) * 2 / 3])
right = SCALE * array([1, -sqrt(3) / 3])

draw_koch(left, apex, DEPTH)
draw_koch(apex, right, DEPTH)
draw_koch(right, left, DEPTH)

t.done()
