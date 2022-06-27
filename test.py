from manim import *


class Graphing(Scene):
    def construct(self):

        plane = (NumberPlane(
            x_range=[-4, 4, 4], x_length = 8, y_range=[-2, 16, 16],
             y_length=18).to_edge(DOWN).add_coordinates())

        labels = plane.get_axis_labels(x_labels="x", y_label="f(x)")

        parab = plane.plot(lambda x : x ** 2, x_range = [-4, 4], color =  GREEN)
    
        self.play(DrawBorderThenFill(plane))
        self.play(Create(VGroup(labels, parab)))
        self.wait()