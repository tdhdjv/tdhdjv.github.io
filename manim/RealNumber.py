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

class Addition(Scene):
    def construct(self):
        positiveNumbers = NumberLine(
            x_range=[-6,6,1],
            length=13.0,
            unit_size=1.0,
            include_ticks=True,
            include_numbers=True,
            tick_size=0.1,
            numbers_with_elongated_ticks=np.arange(-6, 7, 1),
            numbers_to_include=np.arange(-6, 7, 1),
            stroke_width=2.0,
        )
        equation = Text(
            "1+2=3",
            t2c={
                '[:1]': BLUE.to_hex(),
                '[2:3]': YELLOW.to_hex(),
                '[4:5]':GREEN.to_hex()},
        ).scale(0.8).move_to(RIGHT*3.0+UP*2.0)

        self.add(positiveNumbers)
        self.add(equation)
        one_arrow = Arrow(
            start=positiveNumbers.number_to_point(0.0),
            end=positiveNumbers.number_to_point(1.0),
            stroke_width=5.0,
            buff=1.0,
            color=BLUE,
        )
        two_arrow = Arrow(
            start=positiveNumbers.number_to_point(1.0),
            end=positiveNumbers.number_to_point(3.0),
            stroke_width=5.0,
            buff=2.0,
            color=YELLOW,
        )
        three_arrow = Arrow(
            start=positiveNumbers.number_to_point(0.0),
            end=positiveNumbers.number_to_point(3.0),
            stroke_width=5.0,
            buff=3.0,
            color=GREEN,
        )

        one_text = Text(
            "1",
            color=BLUE
        ).scale(0.8).next_to(one_arrow, direction=UP)

        two_text = Text(
            "2",
            color=YELLOW
        ).scale(0.8).next_to(two_arrow, direction=UP)

        three_text = Text(
            "3",
            color=GREEN
        ).scale(0.8).next_to(three_arrow, direction=UP)

        one = Group(one_arrow, one_text)
        two = Group(two_arrow, two_text)
        one_plus_two = Group(one, two)

        three = Group(three_arrow, three_text)
        
        self.play(Create(one_arrow), run_time=0.3)
        self.play(Write(one_text), run_time=0.3)
        self.play(Create(two_arrow), run_time=0.3)
        self.play(Write(two_text), run_time=0.3)
        self.play(Transform(one_plus_two, three))
        self.wait(0.3)

class Multiply(Scene):
    def construct(self):
        positiveNumbers = NumberLine(
            x_range=[-6,6,1],
            length=13.0,
            unit_size=1.0,
            include_ticks=True,
            include_numbers=True,
            tick_size=0.1,
            numbers_with_elongated_ticks=np.arange(-6, 7, 1),
            numbers_to_include=np.arange(-6, 7, 1),
            stroke_width=2.0,
        )
        equation = Text(
            "1.5*2=3",
            t2c={
                '[:3]': BLUE.to_hex()
            }
        ).scale(0.8).move_to(RIGHT*3.0+UP*2.0)
        arrow = Arrow(
            start=positiveNumbers.number_to_point(0.0),
            end=positiveNumbers.number_to_point(1.5),
            stroke_width=5.0,
            buff=1.5,
            color=BLUE,
        )
        
        tracker = ValueTracker(0)
        tracker.set_value(1.5)

        decimal = DecimalNumber(1.5).scale(0.8).next_to(arrow, UP)
        
        self.add(positiveNumbers)
        self.add(equation)
        self.play(GrowArrow(arrow))
        self.play(Write(decimal))
        
        def update(mob):
            mob.set_value(tracker.get_value())
            mob.next_to(arrow, UP)

        decimal.add_updater(
            update
        )
        arrow.add_updater(
            lambda mob: mob.put_start_and_end_on(
                positiveNumbers.number_to_point(0.0),
                positiveNumbers.n2p(tracker.get_value()),            
            )
        )
        self.play(tracker.animate.set_value(3.0))
        self.wait(0.5)
