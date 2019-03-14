import turtle as t
from math import sqrt


t.hideturtle()
t.color('red')
t.speed(0)


def draw_triangle(p1: t.Vec2D, p2: t.Vec2D, p3: t.Vec2D, depth: int) -> None:
    p1p2 = p2 - p1
    p2p3 = p3 - p2
    p1p3 = p3 - p1
    if depth == 0:
        t.penup()
        t.goto(p1)
        t.pendown()
        t.goto(p2)
        t.goto(p3)
        t.goto(p1)
    else:
        # draw_triangle(p1, p1 + p1p2 * (1 / 2), p1 + p1p3 * (1 / 2), 0)
        # draw_triangle(p1 + p1p2 * (1 / 2), p2, p2 + p2p3 * (1 / 2), 0)
        # draw_triangle(p1 + p1p3 * (1 / 2), p2 + p2p3 * (1 / 2), p3, 0)
        draw_triangle(p1, p1 + p1p2 * (1 / 2), p1 + p1p3 * (1 / 2), depth - 1)
        draw_triangle(p1 + p1p2 * (1 / 2), p2, p2 + p2p3 * (1 / 2), depth - 1)
        draw_triangle(p1 + p1p3 * (1 / 2), p2 + p2p3 * (1/2), p3, depth - 1)


DEPTH = 7
SCALE = 300

t.Vec2D(-1, -sqrt(3) / 3)

left = SCALE * t.Vec2D(-1, -sqrt(3) / 2)
apex = SCALE * t.Vec2D(0, sqrt(3) / 2)
right = SCALE * t.Vec2D(1, -sqrt(3) / 2)

draw_triangle(left, apex, right, DEPTH)

t.done()
