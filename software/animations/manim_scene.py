
from manim import *

class ProcessOntologyAttractorScene(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        title = Text("Process Ontology: Attractor Basin X* Contracting", font_size=24)
        title.to_corner(UL)
        self.add_fixed_in_frame_mobjects(title)

        # Plot 3D Conformal Attractor Curve
        curve = ParametricFunction(
            lambda t: np.array([
                (0.618 + 0.5 * np.exp(-0.2 * t)) * np.cos(t),
                (0.618 + 0.5 * np.exp(-0.2 * t)) * np.sin(t),
                0.5 + 0.00086844 * np.sin(10 * t)
            ]),
            t_range=[0, 4 * PI],
            color=GOLD
        )

        self.play(Create(axes), Create(curve), run_time=5)
        self.wait(1)
