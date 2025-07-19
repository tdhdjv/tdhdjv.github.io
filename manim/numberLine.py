from manim import *

class NumberLineGeneration(Scene):
    def construct(self):
        zero = Text("0", font_size=25)
        self.play(Write(zero))
        self.play(zero.animate.move_to(DOWN*0.2), run_time=0.2);
        
        zero_tick = Line(ORIGIN+UP*0.35, ORIGIN+DOWN*0.01, stroke_width=2.0);

        self.play(Create(zero_tick), run_time=0.1);

        positiveNumbers = NumberLine(
            x_range=[0,7,1],
            length=7.0,
            unit_size=1.0,
            include_ticks=True,
            include_numbers=True,
            tick_size=0.1,
            numbers_with_elongated_ticks=np.arange(0, 7, 1),
            include_tip=True,
            numbers_to_include=np.arange(1, 6, 1),
            stroke_width=2.0,
        ).move_to(RIGHT*3.5)

        positiveNumbers.add_labels(dict_values={6.0: "..."}, buff=0.4,font_size=30)

        self.play(Create(positiveNumbers))
        self.wait(0.5);

        negativeNumbers = NumberLine(
            x_range=[-6, 1,1],
            length=7.0,
            unit_size=1.0,
            include_ticks=True,
            include_numbers=True,
            tick_size=0.1,
            numbers_with_elongated_ticks=np.arange(-6, 1, 1),
            include_tip=True,
            numbers_to_include=np.arange(-1, -6, -1),
            rotation=180*DEGREES,
            stroke_width = 2.0,
        ).move_to(LEFT*3.5)

        negativeNumbers.add_labels(dict_values={0: "..."}, buff=0.4,font_size=30)

        self.play(Create(negativeNumbers, reverse=True))
        self.wait(2.0)
