import Mathlib.Analysis.SpecialFunctions.Pow.Real

/-!
# Decoherence: Quantum Zeno Decoherence Floor
-/

set_option linter.style.header false

/--
The survival probability of a quantum state in the quadratic Zeno regime.
-/
noncomputable def survival_prob_Zeno (t : ℝ) (tau_Z : ℝ) : ℝ := 1 - t ^ 2 / tau_Z ^ 2

/--
The universal decoherence rate $\gamma_{\text{dec}}$ resulting from measurements at scale $\tau_0$.
-/
noncomputable def gamma_dec (tau_0 : ℝ) (tau_Z : ℝ) : ℝ := tau_0 / tau_Z ^ 2
