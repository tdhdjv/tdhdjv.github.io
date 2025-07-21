from manim import *

class CoordinatePlane(Scene) :
    def construct(self):
        x_axis = NumberLine(
            x_range=[-6,6,1],
            length=13.0,
            unit_size=1.0,
            include_ticks=True,
            include_numbers=True,
            tick_size=0.1,
            numbers_with_elongated_ticks=np.arange(-6, 7, 1),
            numbers_to_include=np.arange(-6, 7, 1),
            stroke_width=2.0,
        ).move_to(UP)

        y_axis = NumberLine(
            x_range=[-6,6,1],
            length=13.0,
            unit_size=1.0,
            include_ticks=True,
            include_numbers=True,
            tick_size=0.1,
            numbers_with_elongated_ticks=np.arange(-6, 7, 1),
            numbers_to_include=np.arange(-6, 7, 1),
            stroke_width=2.0,
        ).move_to(DOWN)

        x_arrow = Arrow(
            start=x_axis.number_to_point(0.0),
            end=x_axis.number_to_point(2.0),
            stroke_width=5.0,
            buff=2.0,
            color=BLUE,
        )
        y_arrow = Arrow(
            start=y_axis.number_to_point(0.0),
            end=y_axis.number_to_point(4.0),
            stroke_width=5.0,
            buff=4.0,
            color=YELLOW,
        )

        text = MathTex(
            "(2,4)", 
            tex_to_color_map={
                "2":BLUE, "4":YELLOW
            }
        ).move_to(UP*3.0 + RIGHT*6.0)
        
        self.add(text)
        self.add(x_axis)
        self.add(y_axis)
        self.play(GrowArrow(x_arrow))
        self.play(GrowArrow(y_arrow))
        self.wait(0.1)
        
        axes = Axes(
            x_range=[-8,8,1],
            y_range=[-6,6,1],
            x_length=8.0,
            y_length=6.0,
            axis_config={"include_numbers":True}
        ).add_coordinates()
        x_y_axis = Group(x_axis, y_axis)
        
        new_x_arrow = Arrow(
            start=axes.coords_to_point(0,0),
            end=axes.coords_to_point(2,0),
            stroke_width=5.0,
            buff=2.0,
            color=BLUE
        )

        new_y_arrow = Arrow(
            start=axes.coords_to_point(0,0),
            end=axes.coords_to_point(0,4),
            stroke_width=5.0,
            buff=4.0,
            color=YELLOW
        )

        self.play(
          Transform(x_y_axis, axes), 
          Transform(x_arrow, new_x_arrow),
          Transform(y_arrow, new_y_arrow)
        )
        coord = Dot(point=axes.coords_to_point(2,4))
        lines = axes.get_lines_to_point(coord.get_center())
        self.play(
            Create(coord),
            Create(lines),
        )
        self.play(text.animate.next_to(coord, (UP+RIGHT)*0.5).scale(0.6))
        self.wait(0.5)

class Addition(Scene):
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

class AdditionDistribute(Scene):
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

class Scaling(Scene):
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

