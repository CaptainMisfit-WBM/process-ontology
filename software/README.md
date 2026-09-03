# Process Ontology Software & Simulation Suite

This directory contains the computational simulation tools, active inference models, and interactive Jupyter notebook environments for Process Ontology.

---

## 📂 Directory Layout

* **[`notebooks/`](notebooks/)**: Interactive visual studios and exploratory computing tools.
  * **[`Process_Ontology_Hypergraph_Studio.ipynb`](notebooks/Process_Ontology_Hypergraph_Studio.ipynb)**: Hypergraph boundary topology and matrix visualization suite.
* **[`active_inference/`](active_inference/)**: Active Inference & Free Energy Principle (FEP) simulation engines.
  * **[`fep_ego_awareness_sim.py`](active_inference/fep_ego_awareness_sim.py)**: Executable Python simulation modeling the Dualist Engine ($\mathcal{Y}^+$ Ego action sampling vs. $\mathcal{Y}^-$ Awareness auditing) under Karl Friston's Free Energy Principle.

---

## ⚡ Active Inference Simulation

To run the Ego/Awareness Free Energy minimization simulation:

```bash
python3 software/active_inference/fep_ego_awareness_sim.py
```

The script simulates cognitive proper time step progression ($\tau_c$), computing variational free energy ($F$), perception updates, and convergence to the Master Postulate attractor basin ($X^*$).
