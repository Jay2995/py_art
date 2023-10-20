from turtle import Turtle, Screen;
import turtle;
import random;
from extract import rgb_colors

turtle.colormode(255)
pointer = Turtle();
pointer.pu()
pointer.speed(0);
pointer.hideturtle();
pointer.setheading(225);
pointer.forward(300);
pointer.setheading(0);


# pointer.pensize(20)
number_of_dots = 5000;

for x in range(1, number_of_dots +1):
    color = random.choice(rgb_colors);
    pointer.dot(10, color);
    pointer.forward(10);
    if x % 50 == 0:
        pointer.setheading(90);
        pointer.forward(10);
        pointer.setheading(180);
        pointer.forward(500);
        pointer.setheading(0);




screen = Screen();
screen.exitonclick();