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

