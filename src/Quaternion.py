from manim import *  # pyright: ignore[reportWildcardImportFromLibrary]


class QuaternionVisualization(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        labels = axes.get_axis_labels(x_label="i", y_label="j", z_label="k")
        self.add(axes)
        self.add(labels)
        self.set_camera_orientation(phi=45 * DEGREES, theta=-120 * DEGREES)

        number = MathTex(
            "1",
            "+",
            "i",
            "+",
            "3j",
            "+",
            "2k",
        )
        number.set_color_by_tex("i", RED)
        number.set_color_by_tex("3j", GREEN)
        number.set_color_by_tex("2k", BLUE)
        arrow = Arrow3D(axes.c2p(0, 0, 0), axes.c2p(1, 3, 2), color=YELLOW)
        x_basis = Arrow3D(axes.c2p(0, 0, 0), axes.c2p(1, 0, 0), color=RED)
        y_basis = Arrow3D(axes.c2p(0, 0, 0), axes.c2p(0, 3, 0), color=GREEN)
        z_basis = Arrow3D(axes.c2p(0, 0, 0), axes.c2p(0, 0, 2), color=BLUE)
        number.to_corner(UR)
        self.add_fixed_in_frame_mobjects(number)
        self.play(
            Create(arrow),
            Create(x_basis),
            Create(y_basis),
            Create(z_basis),
            Write(number),
        )
        self.move_camera(theta=2 * PI, run_time=PI * 2.0, rate_func=smoothstep)


class QuaternionRotation(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=[-4, 4, 1], y_range=[-4, 4, 1], x_length=8.0, y_length=8.0
        )
        xlabel = axes.get_x_axis_label(label="j")
        ylabel = axes.get_y_axis_label(label="k", rotation=0)
        zlabel = axes.get_z_axis_label(label="i")

        arrow = Arrow3D(axes.c2p(0, 0, 0), axes.c2p(1, 0, 0), color=YELLOW)

        arrow1 = Arrow3D(axes.c2p(0, 0, 0), axes.c2p(2, 3, 0), color=BLUE)
        basis1 = Arrow3D(axes.c2p(0, 0, 0), axes.c2p(2, 0, 0), color=RED)
        basis2 = Arrow3D(axes.c2p(0, 0, 0), axes.c2p(0, 3, 0), color=GREEN)

        label = MathTex("j", color=YELLOW).move_to(axes.c2p(0.5, 0) + 0.5 * UP)
        label1 = MathTex(r"i{\cdot}j", color=YELLOW).move_to(
            axes.c2p(0.5, 0, 0) + 0.5 * UP
        )
        label2 = MathTex("k", color=YELLOW).move_to(axes.c2p(0, 0.5) + 0.5 * LEFT)
        label3 = MathTex(r"i{\cdot}k", color=YELLOW).move_to(
            axes.c2p(0, 0.5) + 0.5 * LEFT
        )
        label4 = MathTex("-j", color=YELLOW).move_to(axes.c2p(-0.5, 0) + 0.5 * UP)

        anotherLabel = MathTex("2j+3k", color=BLUE).move_to(axes.c2p(1, 1.5) + RIGHT)
        anotherLabel1 = MathTex("-3j+2k", color=BLUE).move_to(axes.c2p(-1.5, 1) + UP)

        self.add(axes)
        self.add(xlabel)
        self.add(ylabel)
        self.add(zlabel)
        self.set_camera_orientation(phi=45 * DEGREES, theta=30 * DEGREES)
        self.play(Create(arrow))

        self.move_camera(phi=0, theta=0, gamma=90 * DEGREES)
        self.play(Write(label))
        self.play(Transform(label, label1))
        self.play(
            Rotate(
                arrow,
                90 * DEGREES,
                axis=OUT,
                about_point=axes.c2p(0, 0, 0),  # pyright: ignore[reportArgumentType]
            ),
            Transform(label, label2),
        )
        self.wait(0.1)
        self.play(Transform(label, label3))
        self.play(
            Rotate(
                arrow,
                90 * DEGREES,
                axis=OUT,
                about_point=axes.c2p(0, 0, 0),  # pyright: ignore[reportArgumentType]
            ),
            Transform(label, label4),
        )
        self.play(Uncreate(arrow), Uncreate(label))
        self.wait(0.2)
        self.play(Create(arrow1), Create(basis1), Create(basis2), Write(anotherLabel))
        self.play(
            Rotate(
                arrow1,
                angle=90 * DEGREES,
                about_point=axes.c2p(0, 0),  # pyright: ignore[reportArgumentType]
            ),  # pyright: ignore[reportArgumentType]
            Rotate(
                basis1,
                angle=90 * DEGREES,
                about_point=axes.c2p(0, 0),  # pyright: ignore[reportArgumentType]
            ),  # pyright: ignore[reportArgumentType]
            Rotate(
                basis2,
                angle=90 * DEGREES,
                about_point=axes.c2p(0, 0, 0),  # pyright: ignore[reportArgumentType]
            ),  # pyright: ignore[reportArgumentType]
            Transform(anotherLabel, anotherLabel1),
        )
        self.wait(0.5)


class QuaternionEIPi(Scene):
    def construct(self):
        numberPlane = NumberPlane(
            x_range=[-6, 6, 1],
            y_range=[-3, 3, 1],
            x_length=12.0,
            y_length=6.0,
        )
        labels = numberPlane.get_axis_labels(x_label="j", y_label="k")

        tracker = ValueTracker()
        tracker.set_value(0.0)

        equation = MathTex(
            r"f(t)=q{\cdot}e^{{i}t}",
            font_size=72,
            color=YELLOW,
        ).move_to(UP * 3.5 + RIGHT * 4.5)
        x_is_equal_to = MathTex("t=", font_size=72).move_to(
            equation.get_center() + DOWN * 0.8 + LEFT * 0.8
        )
        digit = DecimalNumber(tracker.get_value(), font_size=72).next_to(
            x_is_equal_to, RIGHT
        )
        arrow = Arrow(
            numberPlane.c2p(0, 0),
            numberPlane.c2p(1, 2),
            buff=0,
            color=YELLOW,
        )
        label = MathTex("q=j+2k", color=YELLOW).move_to(1.2 * numberPlane.c2p(1, 2))

        self.add(numberPlane)
        self.add(equation)
        self.add(labels)
        self.add(x_is_equal_to)
        self.add(digit)
        self.play(GrowArrow(arrow), Write(label))
        self.wait(0.2)
        self.play(
            Transform(
                label,
                MathTex("f(t)", color=YELLOW).move_to(1.2 * numberPlane.c2p(1, 2)),
            )
        )

        arrow.add_updater(
            lambda mob: mob.put_start_and_end_on(
                numberPlane.c2p(0, 0),
                numberPlane.c2p(
                    np.cos(tracker.get_value()) - 2 * np.sin(tracker.get_value()),
                    2 * np.cos(tracker.get_value()) + np.sin(tracker.get_value()),
                ),
            )
        )
        label.add_updater(
            lambda mob: mob.move_to(
                numberPlane.c2p(
                    1.2
                    * (np.cos(tracker.get_value()) - 2 * np.sin(tracker.get_value())),
                    1.2
                    * (2 * np.cos(tracker.get_value()) + np.sin(tracker.get_value())),
                )
            )
        )
        digit.add_updater(lambda mob: mob.set_value(tracker.get_value()))
        self.play(tracker.animate.set_value(10.0), run_time=3.0, rate_func=smoothstep)
        self.wait(0.2)


class WrongTurn(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=60 * DEGREES, theta=30 * DEGREES)

        tracker = ValueTracker()
        labels = axes.get_axis_labels(x_label="i", y_label="j", z_label="k")
        equation = MathTex(r"i{\cdot}e^{i{t}}", font_size=72, color=YELLOW).to_corner(
            UR
        )
        x_is_equal_to = MathTex("t=", font_size=50).move_to(
            equation.get_center() + DOWN * 0.8 + LEFT * 0.8
        )
        digit = DecimalNumber(tracker.get_value(), font_size=50).next_to(
            x_is_equal_to, RIGHT
        )

        arrow = Arrow3D(axes.c2p(0, 0, 0), axes.c2p(1, 0, 0), color=YELLOW)

        self.add(axes)
        self.add(labels)
        self.add(arrow)
        self.add_fixed_in_frame_mobjects(equation)
        self.add_fixed_in_frame_mobjects(x_is_equal_to)
        self.add_fixed_in_frame_mobjects(digit)

        arrow.add_updater(
            lambda mob: mob.put_start_and_end_on(
                axes.c2p(0, 0, 0),
                axes.c2p(np.cos(tracker.get_value()), 0, 0),
            )
        )

        def update(mob):
            mob.set_value(tracker.get_value())
            self.add_fixed_in_frame_mobjects(mob)

        digit.add_updater(update)
        curved = CurvedArrow(UP * 0.5, OUT * 0.5, radius=0.5)
        curved1 = CurvedArrow(DOWN * 0.5, IN * 0.5, radius=0.5)
        self.add(curved)
        self.add(curved1)
        self.play(tracker.animate.set_value(2 * PI), run_time=PI, rate_func=linear)


class Why(Scene):
    def construct(self):
        axes = (
            ThreeDAxes(
                x_range=[-3, 3, 1],
                y_range=[-3, 3, 1],
                z_range=[-3, 3, 1],
                x_length=6,
                y_length=6,
                z_length=6,
            )
            .to_edge(RIGHT)
            .rotate(-50 * DEGREES, UP)
            .rotate(45 * DEGREES, LEFT)
        )
        numberPlane = NumberPlane(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1], x_length=6, y_length=6
        ).to_edge(LEFT)

        tracker = ValueTracker()
        labels = numberPlane.get_axis_labels(x_label="1", y_label="i")
        equation = MathTex(r"i{\cdot}e^{i{t}}", font_size=72, color=YELLOW).to_corner(
            UR
        )
        x_is_equal_to = MathTex("t=", font_size=50).move_to(
            equation.get_center() + DOWN * 0.8 + LEFT * 0.8
        )
        digit = DecimalNumber(tracker.get_value(), font_size=50).next_to(
            x_is_equal_to, RIGHT
        )

        arrow = Arrow3D(axes.c2p(0, 0, 0), axes.c2p(1, 0, 0), color=RED)
        arrow2d = Arrow(
            numberPlane.c2p(0, 0), numberPlane.c2p(0, 1), buff=0, color=YELLOW
        )
        imaginary_basis = Arrow(
            numberPlane.c2p(0, 0), numberPlane.c2p(0, 1), buff=0, color=RED
        )

        self.add(axes)
        self.add(numberPlane)
        self.add(labels)
        self.add(arrow)
        self.add(arrow2d)
        self.add(imaginary_basis)
        self.add(equation)
        self.add(x_is_equal_to)
        self.add(digit)
        arrow.add_updater(
            lambda mob: mob.put_start_and_end_on(
                axes.c2p(0, 0, 0),
                axes.c2p(np.cos(tracker.get_value()), 0, 0),
            )
        )
        arrow2d.add_updater(
            lambda mob: mob.put_start_and_end_on(
                numberPlane.c2p(0, 0),
                numberPlane.c2p(
                    np.sin(tracker.get_value()),
                    np.cos(tracker.get_value()),
                ),
            )
        )
        imaginary_basis.add_updater(
            lambda mob: mob.put_start_and_end_on(
                numberPlane.c2p(0, 0),
                numberPlane.c2p(0, np.cos(tracker.get_value())),
            )
        )

        digit.add_updater(lambda mob: mob.set_value(tracker.get_value()))
        self.play(tracker.animate.set_value(2 * PI), run_time=PI, rate_func=linear)
