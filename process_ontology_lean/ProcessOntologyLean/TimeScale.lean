import ProcessOntologyLean.ConformalScaling
import ProcessOntologyLean.VacuumIntegrity

/-!
# Time Scale: Planck Time and the Fractal Stutter
-/

set_option linter.style.header false

open Real

/--
The Planck time unit constant $t_P \approx 5.391 \times 10^{-44} \text{ s}$.
-/
def t_P : ℝ := 5.391e-44

/--
The duration of one universal recursive frame update $\tau_0$.
-/
noncomputable def tau_0 (P : ℝ) : ℝ :=
  t_P * phi ^ (lambda_vac P)
