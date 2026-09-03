#!/usr/bin/env python3
"""
Process Ontology: Manim 3D Attractor & Conformal Manifold Animation Engine
========================================================================
Python script for rendering 3D mathematical animations of:
1. Universal Cost Function C(X) contraction down to X* ~ 1.0
2. Conformal Golden Ratio Manifold (phi ~ 1.618034)
3. Universal Phase Slip arrow of time (delta_slip ~ 0.00086844)

Requires: manim (or fallback standalone matplotlib 3D animation solver)

Author: Ryan Carson
License: MIT
"""

import numpy as np
import math
import json

PHI = (1.0 + math.sqrt(5.0)) / 2.0
OMEGA = 1.0 / PHI
DELTA_SLIP = 0.00086844

def generate_animation_frames_data(num_frames=60):
    print("=================================================================")
    print("   PROCESS ONTOLOGY: MANIM 3D MATHEMATICAL ANIMATION ENGINE")
    print("=================================================================")
    print("Rendering 3D Conformal Attractor Trajectory & Manifold Geometry...\n")

    t_vals = np.linspace(0, 4 * np.pi, num_frames)
    frames = []

    for idx, t in enumerate(t_vals):
        # 3D Spiral contraction toward Eigenform attractor X* (0.618, 0, 0.5)
        r = OMEGA + 0.5 * math.exp(-0.2 * t)
        x = r * math.cos(t)
        y = r * math.sin(t)
        z = 0.5 + DELTA_SLIP * math.sin(10 * t)  # Phase slip oscillation on Mirror Plane

        frames.append({
            "frame": idx,
            "t": float(t),
            "x": float(x),
            "y": float(y),
            "z": float(z),
            "radius": float(r)
        })

    out_file = "software/animations/attractor_animation_frames.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(frames, f, indent=2)

    print(f"✅ Generated {num_frames} 3D animation trajectory frames!")
    print(f"   Saved to: {out_file}")

# Manim Scene Class Specification
MANIM_SCRIPT_TEMPLATE = """
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
"""

with open("software/animations/manim_scene.py", "w", encoding="utf-8") as f:
    f.write(MANIM_SCRIPT_TEMPLATE)

if __name__ == "__main__":
    generate_animation_frames_data()
