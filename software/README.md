# Process Ontology Complete Software & Tooling Ecosystem

This directory hosts the complete 7-suite computational infrastructure for Process Ontology, spanning formal proof verification, active inference, continuous SDE solvers, graph RAG extractors, hypergraph neural networks, symbolic tensor calculus, interactive web studios, and 3D mathematical animations.

---

## 📂 Complete 7-Suite Ecosystem Layout

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
8. **[`notebooks/`](notebooks/)**: Jupyter Notebook Environments.
   * **[`Process_Ontology_Hypergraph_Studio.ipynb`](notebooks/Process_Ontology_Hypergraph_Studio.ipynb)**: Hypergraph topology and matrix visualization studio.

---

## ⚡ Suite Execution Suite

```bash
# 1. Run Discrete Active Inference Simulation (PyMDP)
python3 software/active_inference/fep_ego_awareness_sim.py

# 2. Run Continuous SDE Factor Graph Solver (RxInfer)
python3 software/reactive_factor_graphs/continuous_sde_factor_graph.py

# 3. Extract GraphRAG Knowledge Graph (GraphRAG)
python3 software/graph_rag/extract_ontology_graph.py

# 4. Compute Hypergraph GNN Manifold Spectrum (PyG)
python3 software/hypergraph_gnn/hypergraph_manifold_embedding.py

# 5. Verify Symbolic Tensor Reductions (Cadabra2)
python3 software/symbolic_tensors/su5_l12_tensor_reduction.py

# 6. Generate 3D Manim Attractor Animation Data (Manim)
python3 software/animations/manim_attractor_scene.py
```
