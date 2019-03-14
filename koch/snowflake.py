import turtle as t
from math import sqrt


t.hideturtle()
t.color('red')
t.speed(0)


def draw_koch(p1: t.Vec2D, p2: t.Vec2D, depth: int) -> None:
    diff = p2 - p1
    b1 = p1 + diff * (1/3)
    b2 = p2 - diff * (1/3)
    apex = b1 + diff.rotate(60) * (1/3)
    if depth == 0:
        t.penup()
        t.goto(p1)
        t.pendown()
        t.goto(p2)
    else:
        draw_koch(p1, b1, depth - 1)
        draw_koch(b1, apex, depth - 1)
        draw_koch(apex, b2, depth - 1)
        draw_koch(b2, p2, depth - 1)


DEPTH = 5
SCALE = 256

t.Vec2D(-1, -sqrt(3) / 3)

left = SCALE * t.Vec2D(-1, -sqrt(3) / 3)
apex = SCALE * t.Vec2D(0, sqrt(3) * 2 / 3)
right = SCALE * t.Vec2D(1, -sqrt(3) / 3)

draw_koch(left, apex, DEPTH)
draw_koch(apex, right, DEPTH)
draw_koch(right, left, DEPTH)

t.done()
