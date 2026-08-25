import Mathlib.Analysis.SpecialFunctions.Pow.Real
import ProcessOntologyLean.ConformalScaling

/-!
# Fermion Generations: S₅ to SU(5) Decompositions
-/

set_option linter.style.header false

open Real

/--
The number of fundamental fermion generations $N_{\text{gen}}$ is the index of the non-solvable
alternating subgroup $A_5 \subset S_5$ decomposed across the conformal interface $\phi$:
$N_{\text{gen}} = \lfloor \frac{120}{60 \cdot \phi} \rfloor + 2 = 3$
-/
noncomputable def N_gen : ℤ := ⌊(120 : ℝ) / (60 * phi)⌋ + 2

/--
Verification that the fermion generations equation resolves to exactly 3.
-/
theorem N_gen_eq_three : N_gen = 3 := by
  unfold N_gen phi
  have h_eq : (120 : ℝ) / (60 * ((1 + Real.sqrt 5) / 2)) = 4 / (1 + Real.sqrt 5) := by
    have h1 : 60 * ((1 + Real.sqrt 5) / 2) = 30 * (1 + Real.sqrt 5) := by linarith
    rw [h1]
    have h2 : (120 : ℝ) / (30 * (1 + Real.sqrt 5)) = (30 * 4) / (30 * (1 + Real.sqrt 5)) := by ring
    rw [h2]
    exact mul_div_mul_left 4 (1 + Real.sqrt 5) (by norm_num : (30 : ℝ) ≠ 0)
  rw [h_eq]
  have h_floor : ⌊4 / (1 + Real.sqrt 5)⌋ = 1 := by
    apply Int.floor_eq_iff.mpr
    constructor
    · have h5 : 0 ≤ (5 : ℝ) := by positivity
      have hsq : Real.sqrt 5 < 3 := by
        rw [← Real.sqrt_sq (by positivity : 0 ≤ (3 : ℝ))]
        exact Real.sqrt_lt_sqrt (by positivity) (by linarith)
      have h_denom : 1 + Real.sqrt 5 > 0 := by
        have : Real.sqrt 5 > 0 := Real.sqrt_pos.mpr (by positivity)
        linarith
      rw [le_div_iff₀ h_denom]
      norm_num
      linarith
    · have h5 : 0 ≤ (5 : ℝ) := by positivity
      have hsq : 1 < Real.sqrt 5 := by
        rw [← Real.sqrt_one]
        exact Real.sqrt_lt_sqrt (by positivity) (by linarith)
      have h_denom : 0 < 1 + Real.sqrt 5 := by linarith
      rw [div_lt_iff₀ h_denom]
      ring_nf
      linarith
  rw [h_floor]
  rfl
