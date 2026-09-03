#!/usr/bin/env python3
"""
Process Ontology: Continuous SDE Reactive Factor Graph Engine
=============================================================
Simulates real-time continuous stochastic state evolution over cognitive proper
time tau_c, implementing the stochastic differential equation:
  dX/d(tau_c) = -mu^-1 * grad(C(X)) + sqrt(2 * delta_slip) * xi(tau_c)

Author: Ryan Carson
License: MIT
"""

import numpy as np
import math
import json

PHI = (1.0 + math.sqrt(5.0)) / 2.0
OMEGA = 1.0 / PHI  # Vacuum Integrity Threshold ~0.618034
DELTA_SLIP = 0.00086844
K_DRAG = 0.005744

def cost_function(X, lam=1.0, L12=12):
    """Universal Cost Function C(X)"""
    if X <= 0:
        return 1e6
    term1 = 0.5 * (math.log(X / OMEGA)) ** 2
    term2 = -(lam / (K_DRAG * L12)) * math.log(X / PHI)
    return term1 + term2

def grad_cost(X, lam=1.0, L12=12):
    """Gradient -grad(C(X))"""
    if X <= 0:
        return 0.0
    return (1.0 / X) * math.log(X / OMEGA) - (lam / (X * K_DRAG * L12))

def simulate_continuous_factor_graph(num_steps=100, dt=0.01):
    print("=================================================================")
    print("   PROCESS ONTOLOGY: CONTINUOUS SDE FACTOR GRAPH ENGINE")
    print("=================================================================")
    print(f"SDE: dX/d(tau_c) = -mu^-1 * grad(C(X)) + sqrt(2 * delta_slip) * xi(tau_c)")
    print(f"Constants: Omega = {OMEGA:.6f}, phi = {PHI:.6f}, delta_slip = {DELTA_SLIP}\n")

    X = 1.5  # Initial state coordinate
    mu = 1.0  # Restorative viscosity
    trajectory = []

    print(f"{'Step (tau_c)':<12} | {'State (X)':<14} | {'Cost C(X)':<14} | {'Grad -grad(C)':<16} | {'Phase Slip Noise'}")
    print("-" * 75)

    np.random.seed(42)
    for tau in range(num_steps):
        grad = grad_cost(X)
        noise = math.sqrt(2.0 * DELTA_SLIP) * np.random.normal(0, 1)
        
        # Euler-Maruyama SDE integration step
        dX = (- (1.0 / mu) * grad + noise) * dt
        X_next = X + dX

        cost = cost_function(X)
        if tau % 10 == 0 or tau == num_steps - 1:
            print(f"{tau * dt:<12.2f} | {X:<14.6f} | {cost:<14.6f} | {grad:<16.6f} | {noise:<+.6f}")

        trajectory.append({
            "tau_c": tau * dt,
            "X": float(X),
            "cost": float(cost),
            "grad": float(grad),
            "noise": float(noise)
        })
        X = X_next

    out_file = "software/reactive_factor_graphs/sde_trajectory.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(trajectory, f, indent=2)

    print("-" * 75)
    print(f"🎉 SDE trajectory simulation complete! Saved to {out_file}")

if __name__ == "__main__":
    simulate_continuous_factor_graph()
