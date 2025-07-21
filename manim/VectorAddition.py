from manim import *

class VectorAddition(Scene):
    def construct(self):
        numberPlane = NumberPlane(
            x_range=[-8,8,1],
            y_range=[-6,6,1],
            x_length=16.0,
            y_length=12.0,
        )

        equation = MathTex("(1,2)+(3,1)=(4,3)", tex_to_color_map={"(1,2)": YELLOW, "(3,1)":BLUE, "(4,3)":GREEN}).move_to(UP*3.5+RIGHT*5.0).scale(0.8)

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

class VectorAdditionAgain(Scene):
    def construct(self):
        numberPlane = NumberPlane(
            x_range=[-8,8,1],
            y_range=[-6,6,1],
            x_length=16.0,
            y_length=12.0,
        )

        equation = MathTex("(1,2)+(3,1)=(4,3)", tex_to_color_map={"(1,2)": YELLOW, "(3,1)":BLUE, "(4,3)":GREEN}).move_to(UP*3.5+RIGHT*5.0).scale(0.8)

        arrow1 = Arrow(numberPlane.c2p(0,0), numberPlane.c2p(1,2), buff=0, color=YELLOW)
        arrow2 = Arrow(numberPlane.c2p(1,2), numberPlane.c2p(4,3), buff=0, color=BLUE)

        x_arrow1 = Arrow(numberPlane.c2p(0,0), numberPlane.c2p(1, 0), buff=0, color=YELLOW)
        x_arrow2 = Arrow(numberPlane.c2p(1,2), numberPlane.c2p(4, 2), buff=0, color=BLUE)

        y_arrow1 = Arrow(numberPlane.c2p(1,0), numberPlane.c2p(1, 2), buff=0, color=YELLOW)
        y_arrow2 = Arrow(numberPlane.c2p(4,2), numberPlane.c2p(4, 3), buff=0, color=BLUE)

        arrow3 = Arrow(numberPlane.c2p(0, 0), numberPlane.c2p(4,3), buff=0, color=GREEN)

        self.add(numberPlane)
        self.add(equation)
        self.add(arrow1)
        self.add(arrow2)
        self.add(arrow3)
        self.play(GrowArrow(x_arrow1), GrowArrow(y_arrow1))
        self.play(GrowArrow(x_arrow2), GrowArrow(y_arrow2))
        self.play(x_arrow2.animate.shift(DOWN*2.0), y_arrow1.animate.shift(RIGHT*3.0))
        self.wait(0.5)

class VectorMul(Scene):
    def construct(self):
        numberPlane = NumberPlane(
            x_range=[-8,8,1],
            y_range=[-6,6,1],
            x_length=16.0,
            y_length=12.0,
        )

        equation = MathTex("(2,1)*2=(4,2)", tex_to_color_map={"(2,1)": YELLOW}).move_to(UP*3.5+RIGHT*5.0).scale(0.8)

        arrow = Arrow(numberPlane.c2p(0,0), numberPlane.c2p(2,1), buff=np.sqrt(5)
, color=YELLOW)

        x_arrow = Arrow(numberPlane.c2p(0,0), numberPlane.c2p(2, 0), buff=2.0)
        y_arrow = Arrow(numberPlane.c2p(2,0), numberPlane.c2p(2, 1), buff=1.0)

        tracker = ValueTracker(0)
        tracker.set_value(1.0)

        self.add(numberPlane)
        self.add(equation)

        def update1(mob):
            mob.scale(tracker.get_value())

        def update2(mob):
            mob.scale(tracker.get_value())

        def update3(mob):
            mob.set_

        self.add(arrow)
        self.add(x_arrow)
        self.add(y_arrow)
        self.wait(0.1)

        x_arrow.add_updater(
            lambda mob: mob.put_start_and_end_on(
                start=numberPlane.c2p(0,0),
                end=numberPlane.c2p(2*tracker.get_value(), 0)
            )
        )
        y_arrow.add_updater(
            lambda mob: mob.put_start_and_end_on(
                start=numberPlane.c2p(2*tracker.get_value(),0),
                end=numberPlane.c2p(2*tracker.get_value(), tracker.get_value())
            )
        )
        arrow.add_updater(
            lambda mob: mob.put_start_and_end_on(
                start=numberPlane.c2p(0,0),
                end=numberPlane.c2p(2*tracker.get_value(), tracker.get_value())
            )
        )

        self.play(tracker.animate.set_value(2.0))
        self.wait(0.5)

