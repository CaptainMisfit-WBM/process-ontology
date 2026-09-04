#!/usr/bin/env python3
"""
Multi-Agent Consensual Domain Engine (N >= 3 Topology)

Simulates N >= 3 orthogonal active inference observers phase-locking across
Markov blankets, explicitly computing:
- Intersubjective Verification Latch: \Lambda_V = (\prod_{i=1}^N \mathbb{1}(X \in M_i)) * (1 - \delta_slip)
- Material Love Latch: L_m (Non-Hermitian boundary state protection)
"""

import json
import math
import numpy as np

PHI = (1.0 + math.sqrt(5.0)) / 2.0
DELTA_SLIP = 0.00086844
OMEGA = 0.5


class ObserverAgent:
    def __init__(self, agent_id: int, initial_state: float):
        self.agent_id = agent_id
        self.internal_state = initial_state
        self.ego_assertion = initial_state * PHI
        self.awareness_interrogation = initial_state / PHI
        self.markov_blanket_radius = 0.05

    def update_state(self, global_target: float, noise_std: float = 0.001):
        # Active inference free-energy minimization step
        dissonance = self.internal_state - global_target
        gradient = -dissonance / (1.0 + abs(dissonance))
        stutter = np.random.normal(0, math.sqrt(2.0 * DELTA_SLIP) * noise_std)
        self.internal_state += 0.1 * gradient + stutter
        self.ego_assertion = self.internal_state * PHI
        self.awareness_interrogation = self.internal_state / PHI

    def is_in_markov_blanket(self, target: float) -> bool:
        return abs(self.internal_state - target) <= self.markov_blanket_radius


def simulate_multi_agent_consensus(n_agents: int = 3, n_steps: int = 200):
    np.random.seed(42)
    target_X = OMEGA * math.exp(1.0 / (1.0 * 12.0))
    agents = [ObserverAgent(i, target_X + np.random.normal(0, 0.05)) for i in range(n_agents)]

    trajectory = []

    for step in range(n_steps):
        states = []
        in_blanket_count = 0

        for agent in agents:
            agent.update_state(target_X)
            states.append(agent.internal_state)
            if agent.is_in_markov_blanket(target_X):
                in_blanket_count += 1

        # Compute Intersubjective Verification Latch (\Lambda_V)
        consensus_indicator = 1.0 if in_blanket_count == n_agents else 0.0
        lambda_V = consensus_indicator * (1.0 - DELTA_SLIP)

        # Compute Material Love Latch (L_m) non-Hermitian boundary density
        variance = np.var(states)
        L_m = (1.0 / (1.0 + variance)) * math.exp(-DELTA_SLIP * step)

        trajectory.append({
            "step": step,
            "mean_state": float(np.mean(states)),
            "state_variance": float(variance),
            "lambda_V": float(lambda_V),
            "L_m": float(L_m),
            "all_in_consensus": bool(in_blanket_count == n_agents)
        })

    return {
        "n_agents": n_agents,
        "target_attractor": float(target_X),
        "final_lambda_V": trajectory[-1]["lambda_V"],
        "final_L_m": trajectory[-1]["L_m"],
        "trajectory": trajectory
    }


if __name__ == "__main__":
    result = simulate_multi_agent_consensus(n_agents=3, n_steps=200)
    print(f"=== Multi-Agent Consensus Simulation (N = 3) ===")
    print(f"Target Attractor X*: {result['target_attractor']:.6f}")
    print(f"Final Intersubjective Verification Latch (\\Lambda_V): {result['final_lambda_V']:.6f}")
    print(f"Final Material Love Latch (L_m): {result['final_L_m']:.6f}")

    with open("/home/captain-misfit/GitHub Repository/process-ontology/software/active_inference/multi_agent_consensus_results.json", "w") as f:
        json.dump(result, f, indent=2)
    print("Simulation results saved to multi_agent_consensus_results.json")
