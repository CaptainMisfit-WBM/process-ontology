import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real

/-!
# Axis of Silence: The Mirror Plane Invariant
-/

set_option linter.style.header false

open Real

/--
The Axis of Silence stability theorem:
If the forward conformal flow magnitude $n^\sigma$ balances the backward resolution flow $n^{1-\sigma}$
at any scale $n > 1$, the scaling dimension $\sigma$ must lie exactly on the mirror plane $\sigma = 1/2$.
-/
theorem axis_of_silence (n : ℝ) (hn : 1 < n) (σ : ℝ) (h : n ^ σ = n ^ (1 - σ)) : σ = 1 / 2 := by
  have hlog_pos : 0 < Real.log n := Real.log_pos hn
  have hlog_ne : Real.log n ≠ 0 := ne_of_gt hlog_pos
  have hn_pos : 0 < n := by linarith
  have h_log : Real.log (n ^ σ) = Real.log (n ^ (1 - σ)) := by rw [h]
  rw [Real.log_rpow hn_pos, Real.log_rpow hn_pos] at h_log
  have h_cancel : σ = 1 - σ := mul_right_cancel₀ hlog_ne h_log
  linarith
