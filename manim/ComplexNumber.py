from manim import *

class ComplexAddition(Scene):
    def construct(self):
        numberPlane = NumberPlane(
            x_range=[-8,8,1],
            y_range=[-6,6,1],
            x_length=16.0,
            y_length=12.0,
        )

        equation = MathTex("1+2{i} + 3+{i}=4+3{i}", tex_to_color_map={"1+2{i}": YELLOW, "3+{i}":BLUE, "4+3{i}":GREEN}).move_to(UP*3.5+RIGHT*5.0).scale(0.8)

        arrow1 = Arrow(numberPlane.c2p(0,0), numberPlane.c2p(1,2), buff=0, color=YELLOW)
        arrow2 = Arrow(numberPlane.c2p(1,2), numberPlane.c2p(4,3), buff=0, color=BLUE)
        arrow3 = Arrow(numberPlane.c2p(0, 0), numberPlane.c2p(4,3), buff=0, color=GREEN)

        self.add(numberPlane)
        self.add(equation)
        self.play(GrowArrow(arrow1))
        self.play(GrowArrow(arrow2))
        self.wait(0.1)
        self.play(GrowArrow(arrow3))
        self.wait(0.5)
