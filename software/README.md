# Process Ontology Software & Simulation Ecosystem

This directory hosts the computational engines, active inference models, graph RAG extractors, hypergraph neural networks, continuous factor graph SDE solvers, and interactive web visualizers for Process Ontology.

---

## 📂 Ecosystem Layout

* **[`active_inference/`](active_inference/)**: Active Inference & Free Energy Principle (FEP) Engine.
  * **[`fep_ego_awareness_sim.py`](active_inference/fep_ego_awareness_sim.py)**: Discrete POMDP simulation modeling the Dualist Engine ($\mathcal{Y}^+$ Ego sampling vs. $\mathcal{Y}^-$ Awareness auditing) under Karl Friston's Free Energy Principle ($F$).
* **[`reactive_factor_graphs/`](reactive_factor_graphs/)**: Continuous Reactive Factor Graph Engine.
  * **[`continuous_sde_factor_graph.py`](reactive_factor_graphs/continuous_sde_factor_graph.py)**: Real-time Euler-Maruyama integration of the stochastic differential equation:
    $$\frac{dX}{d\tau_c} = -\mu^{-1}\nabla\mathcal{C}(X) + \sqrt{2\delta_{\text{slip}}}\xi(\tau_c)$$
* **[`graph_rag/`](graph_rag/)**: Hierarchical Knowledge Graph Extractor.
  * **[`extract_ontology_graph.py`](graph_rag/extract_ontology_graph.py)**: Multi-scale entity-relation extraction engine generating `process_ontology_knowledge_graph.json` connecting papers, physical constants, Lean 4 theorems, and empirical tests.
* **[`hypergraph_gnn/`](hypergraph_gnn/)**: PyTorch Geometric (PyG) Manifold Embedding Engine.
  * **[`hypergraph_manifold_embedding.py`](hypergraph_manifold_embedding.py)**: Hypergraph Laplacian spectrum solver projecting the 12 Causal Latch dimensions ($L_{12}$) onto continuous 3D conformal manifolds.
* **[`studio/`](studio/)**: Cytoscape.js Interactive Web Studio.
  * **[`index.html`](studio/index.html)**: Standalone web browser visualizer allowing interactive drag, expansion, and inspection of Process Ontology invariant nodes.
* **[`notebooks/`](notebooks/)**: Jupyter Notebook Environments.
  * **[`Process_Ontology_Hypergraph_Studio.ipynb`](notebooks/Process_Ontology_Hypergraph_Studio.ipynb)**: Hypergraph topology and matrix visualization studio.

---

## ⚡ Execution Commands

```bash
# 1. Run Discrete Active Inference Simulation
python3 software/active_inference/fep_ego_awareness_sim.py

# 2. Run Continuous SDE Factor Graph Solver
python3 software/reactive_factor_graphs/continuous_sde_factor_graph.py

# 3. Extract GraphRAG Knowledge Graph
python3 software/graph_rag/extract_ontology_graph.py

# 4. Compute Hypergraph GNN Manifold Spectrum
python3 software/hypergraph_gnn/hypergraph_manifold_embedding.py
```
