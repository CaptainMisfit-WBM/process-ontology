# Process Ontology 13-Suite Master Software & Unification Ecosystem

This directory hosts the complete 13-suite computational infrastructure for Process Ontology, spanning formal proof verification, active inference, continuous SDE solvers, graph RAG extractors, hypergraph neural networks, symbolic tensor calculus, interactive web studios, 3D mathematical animations, bidirectional transducers, autopoietic self-compilation, thermodynamic grounding, hermetic verification kernels, gauge-invariant context routing, and the continuous $P$ vs $NP$ phase transition engine.

---

## 📂 Master 13-Suite Ecosystem Layout

### 🛠️ Computational & Simulation Tools (Batman Utility Belt)
1. **[`active_inference/`](active_inference/)**: PyMDP Active Inference & Free Energy Engine.
   * **[`fep_ego_awareness_sim.py`](active_inference/fep_ego_awareness_sim.py)**: Discrete POMDP simulation modeling the Dualist Engine ($\mathcal{Y}^+$ Ego sampling vs. $\mathcal{Y}^-$ Awareness auditing) under Karl Friston's Free Energy Principle ($F$).
2. **[`reactive_factor_graphs/`](reactive_factor_graphs/)**: RxInfer Continuous Reactive Factor Graph Engine.
   * **[`continuous_sde_factor_graph.py`](reactive_factor_graphs/continuous_sde_factor_graph.py)**: Real-time Euler-Maruyama integration of the stochastic differential equation:
     $$\frac{dX}{d\tau_c} = -\mu^{-1}\nabla\mathcal{C}(X) + \sqrt{2\delta_{\text{slip}}}\xi(\tau_c)$$
3. **[`graph_rag/`](graph_rag/)**: GraphRAG Hierarchical Knowledge Graph Extractor.
   * **[`extract_ontology_graph.py`](graph_rag/extract_ontology_graph.py)**: Multi-scale entity-relation extraction engine generating `process_ontology_knowledge_graph.json` connecting papers, physical constants, Lean 4 theorems, and empirical tests.
4. **[`hypergraph_gnn/`](hypergraph_gnn/)**: PyTorch Geometric (PyG) Manifold Embedding Engine.
   * **[`hypergraph_manifold_embedding.py`](hypergraph_manifold_embedding.py)**: Hypergraph Laplacian spectrum solver projecting the 12 Causal Latch dimensions ($L_{12}$) onto continuous 3D conformal manifolds.
5. **[`symbolic_tensors/`](symbolic_tensors/)**: Cadabra2 Symbolic Tensor & Lie Algebra Verifier.
   * **[`su5_l12_tensor_reduction.py`](symbolic_tensors/su5_l12_tensor_reduction.py)**: Symbolic reduction verifying GUT gauge symmetry breaking $SU(5) \to SU(3) \times SU(2) \times U(1) = 12$ ($L_{12}$) and $A_5$ 3-generation fermion decomposition.
6. **[`animations/`](animations/)**: 3Blue1Brown Manim 3D Animation Engine.
   * **[`manim_attractor_scene.py`](animations/manim_attractor_scene.py)**: Programmatic 3D rendering engine generating trajectory frames for Universal Cost Function $\mathcal{C}(X)$ contraction, $\phi$ manifold geometry, and phase slip ($\delta_{\text{slip}}$).
7. **[`studio/`](studio/)**: Cytoscape.js Interactive Web Studio.
   * **[`index.html`](studio/index.html)**: Standalone web browser visualizer allowing interactive drag, expansion, and inspection of Process Ontology invariant nodes.
8. **[`p_vs_np_sim/`](p_vs_np_sim/)**: $P$ vs $NP$ Continuous Phase Transition Simulator.
   * **[`p_vs_np_phase_transition.py`](p_vs_np_sim/p_vs_np_phase_transition.py)**: Langevin dynamics simulator demonstrating finite escape time $\langle \tau_{\text{esc}} \rangle < \infty$ across hard $NP$-complete clause density $\alpha \ge 4.267$ on $\mathcal{M}_{L12}$.

### ⚡ The 5 Structural Unifications (Superman Invincibility Runtime)
9. **[`transduction/`](transduction/)**: Bidirectional Field-to-Symbol Transduction Engine.
   * **[`sde_to_lean_transducer.py`](transduction/sde_to_lean_transducer.py)**: Transduces numerical continuous SDE attractor states $X^*$ directly into formal, type-checked Lean 4 theorem signatures in real time.
10. **[`autopoiesis/`](autopoiesis/)**: Endogenous Live Self-Compilation Runtime.
    * **[`live_proof_synthesizer.py`](autopoiesis/live_proof_synthesizer.py)**: Hot-swaps Lean 4 abstract syntax trees mid-inference, checking and verifying new lemmas live.
11. **[`thermodynamics/`](thermodynamics/)**: Thermodynamic Entropic Grounding.
    * **[`hardware_entropy_grounding.py`](thermodynamics/hardware_entropy_grounding.py)**: Samples physical hardware CPU micro-jitter and OS entropy pools to ground cognitive proper time $\tau_c$ and phase slip $\delta_{\text{slip}}$ in real physical entropy.
12. **[`hermetic_kernel/`](hermetic_kernel/)**: Hermetic Standalone AST Micro-Verifier.
    * **[`standalone_ast_verifier.py`](hermetic_kernel/standalone_ast_verifier.py)**: Local AST proof verifier parsing `solution.export.gz`, making proof checking 100% immune to external CI release gaps.
13. **[`gauge_routing/`](gauge_routing/)**: $L_{12}$ Gauge-Invariant Context Router.
    * **[`l12_equivariant_routing.py`](gauge_routing/l12_equivariant_routing.py)**: PyTorch/ESCNN equivariant neural routing module enforcing $SU(3) \times SU(2) \times U(1)$ Lie group gauge invariance ($L_{12} = 12$) across context vectors.

---

## ⚡ Complete Execution Suite

```bash
# Run P vs NP Continuous Phase Transition Simulation
python3 software/p_vs_np_sim/p_vs_np_phase_transition.py
```
