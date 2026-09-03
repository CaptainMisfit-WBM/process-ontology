#!/usr/bin/env python3
"""
Process Ontology: Active Inference & Free Energy Minimization Engine
====================================================================
Simulates the Dualist Engine (Ego / Awareness) dynamics under Karl Friston's
Free Energy Principle (FEP), mapping active inference POMDP policies to
the Universal Solving Equation C(X) cost minimization trajectory.

Author: Ryan Carson
License: MIT
"""

import numpy as np
import math
import json

# Physical & Geometric Constants
PHI = (1.0 + math.sqrt(5.0)) / 2.0  # Conformal Golden Ratio ~1.618034
SIGMA_MIRROR = 0.5                  # Axis of Silence mirror dimension
DELTA_SLIP = 0.00086844             # Universal Slip parameter

class EgoAwarenessActiveInference:
    """
    Active Inference Agent representing the Dualist Engine:
    - Ego (Yang / Positive Pole): Generative Action & Policy Sampling Y+
    - Awareness (Yin / Negative Pole): Observation Auditing & Surprisal Minimization Y-
    """

    def __init__(self, num_states=5, num_obs=5, num_actions=3):
        self.num_states = num_states
        self.num_obs = num_obs
        self.num_actions = num_actions

        # 1. Observation Likelihood Matrix (A Matrix: p(o|s))
        # Identity likelihood with small environmental phase slip delta_slip
        self.A = np.eye(num_obs) * (1.0 - DELTA_SLIP) + (DELTA_SLIP / (num_obs - 1)) * (1.0 - np.eye(num_obs))

        # 2. Transition Dynamics (B Matrix: p(s'|s, a))
        # Action 0: Maintain baseline flow (Neutral Axis of Silence sigma = 0.5)
        # Action 1: Ego Expansion (Yang Flow Y+)
        # Action 2: Awareness Contraction (Yin Audit Y-)
        self.B = np.zeros((num_states, num_states, num_actions))

        for s in range(num_states):
            self.B[s, s, 0] = 1.0  # Baseline stability
            self.B[min(s + 1, num_states - 1), s, 1] = 1.0  # Yang Expansion
            self.B[max(s - 1, 0), s, 2] = 1.0  # Yin Contraction

        # 3. Prior Preferences (C Matrix: p(o))
        # Gaussian preference centered at the attractor basin X* (index num_states//2)
        target_state = num_states // 2
        states = np.arange(num_obs)
        self.C = np.exp(-0.5 * ((states - target_state) / SIGMA_MIRROR) ** 2)
        self.C /= np.sum(self.C)

        # 4. Prior Beliefs (D Matrix: p(s_0))
        self.D = np.ones(num_states) / num_states

        # Active state beliefs q(s)
        self.q_s = np.copy(self.D)

    def calculate_variational_free_energy(self, obs, q_s):
        """
        Calculates Variational Free Energy F:
        F = KL[q(s) || p(s)] - E_q[ln p(o|s)]
        """
        likelihood = self.A[obs, :]
        log_likelihood = np.log(likelihood + 1e-12)
        log_prior = np.log(self.C + 1e-12)

        # Complexity (KL divergence) + Accuracy penalty
        accuracy = -np.sum(q_s * log_likelihood)
        complexity = np.sum(q_s * (np.log(q_s + 1e-12) - log_prior))
        F = accuracy + complexity
        return F

    def step(self, obs, last_action=0):
        """
        Performs one cognitive iteration over cognitive proper time tau_c:
        1. Perception update (Awareness Y- auditing)
        2. Free Energy calculation F
        3. Action selection (Ego Y+ sampling)
        """
        # 1. Perception Update: q(s) = softmax(ln A[obs, :] + ln B[s, s_prev, a] + ln q_s)
        prior_state = np.dot(self.B[:, :, last_action], self.q_s)
        likelihood = self.A[obs, :]
        unnormalized_q = likelihood * prior_state
        self.q_s = unnormalized_q / (np.sum(unnormalized_q) + 1e-12)

        # 2. Calculate Surprisal / Free Energy
        F = self.calculate_variational_free_energy(obs, self.q_s)

        # 3. Action Selection minimizing expected Free Energy G
        # Compare expected free energy under Yang expansion vs Yin audit
        G_actions = np.zeros(self.num_actions)
        for a in range(self.num_actions):
            predicted_q = np.dot(self.B[:, :, a], self.q_s)
            predicted_obs = np.dot(self.A, predicted_q)
            # Expected free energy G
            G_actions[a] = np.sum(predicted_q * (np.log(predicted_q + 1e-12) - np.log(self.C + 1e-12)))

        # Softmax policy selection
        policy_probs = np.exp(-G_actions) / np.sum(np.exp(-G_actions))
        chosen_action = np.argmax(policy_probs)

        return self.q_s, F, chosen_action, policy_probs

def run_simulation(num_steps=20):
    print("=================================================================")
    print("   PROCESS ONTOLOGY: DUALIST ENGINE ACTIVE INFERENCE SIMULATION")
    print("=================================================================")
    print(f"Constants: Conformal Golden Ratio phi = {PHI:.6f}")
    print(f"           Axis of Silence Mirror Plane sigma = {SIGMA_MIRROR}")
    print(f"           Universal Phase Slip delta_slip = {DELTA_SLIP}\n")

    agent = EgoAwarenessActiveInference()
    current_obs = 0  # Initial perturbed observation
    last_action = 0

    history = []
    print(f"{'Step (tau_c)':<12} | {'Obs':<5} | {'Free Energy (F)':<18} | {'Ego/Awareness Action':<22} | {'Attractor Belief'}")
    print("-" * 75)

    for tau in range(num_steps):
        q_s, F, action, probs = agent.step(current_obs, last_action)
        action_name = ["0: Baseline Flow", "1: Ego Sampling (Y+)", "2: Awareness Audit (Y-)"][action]
        best_belief_state = np.argmax(q_s)

        print(f"{tau:<12} | {current_obs:<5} | {F:<18.6f} | {action_name:<22} | State {best_belief_state} (p={q_s[best_belief_state]:.3f})")

        history.append({
            "step": tau,
            "observation": int(current_obs),
            "free_energy": float(F),
            "action": action_name,
            "target_state_probability": float(q_s[2])
        })

        # Environment update based on action
        if action == 1:
            current_obs = min(current_obs + 1, agent.num_obs - 1)
        elif action == 2:
            current_obs = max(current_obs - 1, 0)
        last_action = action

    summary_file = "software/active_inference/simulation_results.json"
    with open(summary_file, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2)

    print("-" * 75)
    print(f"🎉 Simulation completed! Results saved to {summary_file}")
    return history

if __name__ == "__main__":
    run_simulation()
