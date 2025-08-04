from manim import *  # pyright: ignore[reportWildcardImportFromLibrary]


class ComplexAddition(Scene):
    def construct(self):
        numberPlane = NumberPlane(
            x_range=[-8, 8, 1],
            y_range=[-6, 6, 1],
            x_length=16.0,
            y_length=12.0,
        )

        equation = (
            MathTex(
                "1+2{i} + 3+{i}=4+3{i}",
                tex_to_color_map={"1+2{i}": YELLOW, "3+{i}": BLUE, "4+3{i}": GREEN},
            )
            .move_to(UP * 3.5 + RIGHT * 5.0)
            .scale(0.8)
        )

        arrow1 = Arrow(
            numberPlane.c2p(0, 0), numberPlane.c2p(1, 2), buff=0, color=YELLOW
        )
        arrow2 = Arrow(numberPlane.c2p(1, 2), numberPlane.c2p(4, 3), buff=0, color=BLUE)
        arrow3 = Arrow(
            numberPlane.c2p(0, 0), numberPlane.c2p(4, 3), buff=0, color=GREEN
        )

        self.add(numberPlane)
        self.add(equation)
        self.play(GrowArrow(arrow1))
        self.play(GrowArrow(arrow2))
        self.wait(0.1)
        self.play(GrowArrow(arrow3))
        self.wait(0.5)


class ComplexTimesI(Scene):
    def construct(self):
        numberPlane = NumberPlane(
            x_range=[-8, 8, 1],
            y_range=[-6, 6, 1],
            x_length=16.0,
            y_length=12.0,
        )

        arrow = Arrow(
            numberPlane.c2p(0, 0), numberPlane.c2p(1, 0), buff=0, color=YELLOW
        )

        arrow1 = Arrow(numberPlane.c2p(0, 0), numberPlane.c2p(2, 3), buff=0, color=BLUE)
        basis1 = Arrow(numberPlane.c2p(0, 0), numberPlane.c2p(2, 0), buff=0, color=RED)
        basis2 = Arrow(
            numberPlane.c2p(0, 0), numberPlane.c2p(0, 3), buff=0, color=GREEN
        )

        label = MathTex("1", color=YELLOW).move_to(numberPlane.c2p(0.5, 0) + 0.5 * UP)
        label1 = MathTex(r"1{\cdot}i", color=YELLOW).move_to(
            numberPlane.c2p(0.5, 0) + 0.5 * UP
        )
        label2 = MathTex("i", color=YELLOW).move_to(
            numberPlane.c2p(0, 0.5) + 0.5 * LEFT
        )
        label3 = MathTex(r"i{\cdot}i", color=YELLOW).move_to(
            numberPlane.c2p(0, 0.5) + 0.5 * LEFT
        )
        label4 = MathTex("-1", color=YELLOW).move_to(
            numberPlane.c2p(-0.5, 0) + 0.5 * UP
        )

        anotherLabel = MathTex("2+3i", color=BLUE).move_to(
            numberPlane.c2p(1, 1.5) + RIGHT
        )
        anotherLabel1 = MathTex("-3+2i", color=BLUE).move_to(
            numberPlane.c2p(-1.5, 1) + UP
        )

        self.add(numberPlane)
        self.play(GrowArrow(arrow), Write(label))
        self.play(Transform(label, label1))
        self.play(
            arrow.animate.rotate(90 * DEGREES, about_point=numberPlane.c2p(0, 0)),
            Transform(label, label2),
        )
        self.wait(0.1)
        self.play(Transform(label, label3))
        self.play(
            arrow.animate.rotate(90 * DEGREES, about_point=numberPlane.c2p(0, 0)),
            Transform(label, label4),
        )

        self.play(Uncreate(arrow), Uncreate(label))
        self.wait(0.2)

        self.play(
            GrowArrow(arrow1), GrowArrow(basis1), GrowArrow(basis2), Write(anotherLabel)
        )
        self.wait(0.1)
        self.play(
            arrow1.animate.rotate(90 * DEGREES, about_point=numberPlane.c2p(0, 0)),
            basis1.animate.rotate(90 * DEGREES, about_point=numberPlane.c2p(0, 0)),
            basis2.animate.rotate(90 * DEGREES, about_point=numberPlane.c2p(0, 0)),
            Transform(anotherLabel, anotherLabel1),
        )


class ComplexRotation(Scene):
    def construct(self):
        numberPlane = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            x_length=16.0,
            y_length=12.0,
        )

        tracker = ValueTracker()
        tracker.set_value(1.0)

        equation = MathTex(
            "f(t)=e^{{i}t}",
            font_size=72,
            color=BLUE,
        ).move_to(UP * 3.5 + RIGHT * 4.5)
        x_is_equal_to = MathTex("t=", font_size=72).move_to(
            equation.get_center() + DOWN * 0.8 + LEFT * 0.8
        )
        digit = DecimalNumber(tracker.get_value(), font_size=72).next_to(
            x_is_equal_to, RIGHT
        )
        label = MathTex("f(t)", color=BLUE).move_to(
            numberPlane.c2p(
                1.2 * np.cos(tracker.get_value()), 1.2 * np.sin(tracker.get_value())
            )
        )
        arrow = Arrow(
            numberPlane.c2p(0, 0),
            numberPlane.c2p(np.cos(tracker.get_value()), np.sin(tracker.get_value())),
            buff=0,
            color=BLUE,
        )

        velocity = Arrow(
            arrow.get_end(),
            arrow.get_end()
            + numberPlane.c2p(-np.sin(tracker.get_value()), np.cos(tracker.get_value()))
            - numberPlane.c2p(0, 0),
            buff=0,
            color=YELLOW,
        )
        velLabel = MathTex("f'(t)", color=YELLOW).move_to(
            velocity.get_end()
            + 0.2
            * (
                numberPlane.c2p(
                    -np.sin(tracker.get_value()), np.cos(tracker.get_value())
                )
                - numberPlane.c2p(0, 0)
            )
        )

        self.add(numberPlane)
        self.add(equation)
        self.add(x_is_equal_to)
        self.add(digit)
        self.play(GrowArrow(arrow), Write(label))
        self.play(GrowArrow(velocity), Write(velLabel))

        arrow.add_updater(
            lambda mob: mob.put_start_and_end_on(
                numberPlane.c2p(0, 0),
                numberPlane.c2p(
                    np.cos(tracker.get_value()), np.sin(tracker.get_value())
                ),
            )
        )
        velocity.add_updater(
            lambda mob: mob.put_start_and_end_on(
                arrow.get_end(),
                arrow.get_end()
                + numberPlane.c2p(
                    -np.sin(tracker.get_value()), np.cos(tracker.get_value())
                )
                - numberPlane.c2p(0, 0),
            )
        )
        label.add_updater(
            lambda mob: mob.move_to(
                numberPlane.c2p(
                    1.2 * np.cos(tracker.get_value()), 1.2 * np.sin(tracker.get_value())
                )
            )
        )
        velLabel.add_updater(
            lambda mob: mob.move_to(
                velocity.get_end()
                + 0.2
                * (
                    numberPlane.c2p(
                        -np.sin(tracker.get_value()), np.cos(tracker.get_value())
                    )
                    - numberPlane.c2p(0, 0)
                )
            )
        )
        digit.add_updater(lambda mob: mob.set_value(tracker.get_value()))
        self.play(tracker.animate.set_value(10.0), run_time=3.0, rate_func=smoothstep)
        self.wait(0.2)


class Rotation(Scene):
    def construct(self):
        numberPlane = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            x_length=16.0,
            y_length=12.0,
        )

        tracker = ValueTracker()
        tracker.set_value(0.0)

        arrow = Arrow(
            numberPlane.c2p(0, 0),
            numberPlane.c2p(np.cos(tracker.get_value()), np.sin(tracker.get_value())),
            buff=0,
            color=BLUE,
        )

        velocity = Arrow(
            arrow.get_end(),
            arrow.get_end()
            + numberPlane.c2p(-np.sin(tracker.get_value()), np.cos(tracker.get_value()))
            - numberPlane.c2p(0, 0),
            buff=0,
            color=YELLOW,
        )

        circle = Circle(
            2.0,
            color=BLUE,
        )

        self.add(numberPlane, arrow, velocity, circle)

        arrow.add_updater(
            lambda mob: mob.put_start_and_end_on(
                numberPlane.c2p(0, 0),
                numberPlane.c2p(
                    np.cos(tracker.get_value()), np.sin(tracker.get_value())
                ),
            )
        )
        velocity.add_updater(
            lambda mob: mob.put_start_and_end_on(
                arrow.get_end(),
                arrow.get_end()
                + numberPlane.c2p(
                    -np.sin(tracker.get_value()), np.cos(tracker.get_value())
                )
                - numberPlane.c2p(0, 0),
            )
        )
        self.play(tracker.animate.set_value(2 * PI), run_time=PI, rate_func=linear)
