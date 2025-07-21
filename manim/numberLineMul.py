from manim import *

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
