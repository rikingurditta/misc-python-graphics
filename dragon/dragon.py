import turtle as t

ITERATIONS = 23
SCALE = 4

t.hideturtle()
t.color('red')
t.speed(0)

all_headings = [0]
headings = [0]
for _ in range(ITERATIONS):
    temp = [x + 90 for x in all_headings]
    temp.reverse()
    for h in headings:
        t.setheading(h)
        t.forward(SCALE)
    headings = temp
    all_headings.extend(headings)
t.done()
