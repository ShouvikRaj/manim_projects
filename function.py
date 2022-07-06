from calendar import c
from operator import imod
from pydoc import plain
from re import X
from textwrap import fill
from time import sleep
from manim import *

class function(Scene):
    def construct(self):
        ax = Axes(x_range=(-3, 3), y_range=(-3, 3))
        curve = ax.plot(lambda x: (x+2)*x*(x-2)/2, color=RED)
        area = ax.get_area(curve, x_range=(-2, 0), color=RED, opacity=0.5)

        self.play(FadeIn(ax))
        self.play(Create(curve))
        self.play(FadeIn(area))
        self.wait()

class SquareToCircle(Scene):
    def construct(self):
        green_square = Square(color=GREEN, fill_opacity=0.5)
        
        self.play(DrawBorderThenFill(green_square))
        self.wait()

        blue_circle = Circle(color=BLUE, fill_opacity=0.5)
        self.play(Transform(green_square, blue_circle))
        self.wait()

