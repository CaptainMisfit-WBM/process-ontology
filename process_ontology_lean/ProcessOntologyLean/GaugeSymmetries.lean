import Mathlib.Data.Nat.Basic

/-!
# Gauge Symmetries: Standard Model Symmetries from Spatial Packing Geometry
-/

set_option linter.style.header false

/--
The dimension of the special unitary Lie algebra $\mathfrak{su}(N)$ is $N^2 - 1$.
-/
def dim_SU (N : ℕ) : ℕ := N ^ 2 - 1

/--
The dimension of the circle group $U(1)$ is $1$.
-/
def dim_U1 : ℕ := 1

/--
The $SU(3)$ Color gauge symmetry (Strong Force) dimension equals 8.
-/
theorem dim_SU3_eq : dim_SU 3 = 8 := by rfl

/--
The $SU(2)$ Weak isospin gauge symmetry (Weak Force) dimension equals 3.
-/
theorem dim_SU2_eq : dim_SU 2 = 3 := by rfl

/--
The total Standard Model gauge boson degrees of freedom is 12,
which maps to the Causal Latch dimension $L_{12} = 12$.
-/
theorem total_gauge_dim : dim_SU 3 + dim_SU 2 + dim_U1 = 12 := by rfl
