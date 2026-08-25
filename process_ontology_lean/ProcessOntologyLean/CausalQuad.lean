import Mathlib.Data.Real.Basic
import Mathlib.Data.Matrix.Basic

/-!
# Causal Quad: Keldysh Green's Function Representation
-/

set_option linter.style.header false

/--
The Keldysh CTP matrix representation of the Causal Quad.
-/
def G_Keldysh (GR GK GA : ℝ) : Matrix (Fin 2) (Fin 2) ℝ :=
  Matrix.of ![![GR, GK], ![0, GA]]
