document.addEventListener("DOMContentLoaded", function() {
  const cy = cytoscape({
    container: document.getElementById('cy'),
    elements: [
      // Core Invariant Nodes
      { data: { id: 'master', label: 'Master Postulate M(X*) = X*', type: 'core', desc: 'The starting coordinate of Process Ontology verified via Banach fixed-point contraction.' } },
      { data: { id: 'phi', label: 'Golden Ratio φ', type: 'constant', desc: 'Unique positive root of x² - x - 1 = 0 (~1.618034).' } },
      { data: { id: 'omega', label: 'Vacuum Threshold Ω', type: 'constant', desc: '1/φ = φ - 1 (~0.618034).' } },
      { data: { id: 'sigma', label: 'Axis of Silence σ = 1/2', type: 'mirror', desc: 'Neutral mirror plane preserving metric balance.' } },
      { data: { id: 'l12', label: 'Causal Latch L₁₂ = 12', type: 'latch', desc: 'Dimension of Standard Model gauge group SU(3) x SU(2) x U(1).' } },
      { data: { id: 'slip', label: 'Universal Slip δ_slip', type: 'friction', desc: 'Attosecond phase stutter ~0.00086844.' } },

      // Edges
      { data: { source: 'master', target: 'phi', label: 'optimizes' } },
      { data: { source: 'phi', target: 'omega', label: 'inverts' } },
      { data: { source: 'master', target: 'sigma', label: 'balances' } },
      { data: { source: 'master', target: 'l12', label: 'tiles' } },
      { data: { source: 'l12', target: 'slip', label: 'induces' } }
    ],
    style: [
      {
        selector: 'node',
        style: {
          'label': 'data(label)',
          'color': '#ffffff',
          'font-size': '12px',
          'text-valign': 'center',
          'text-halign': 'center',
          'background-color': '#3b82f6',
          'width': '60px',
          'height': '60px',
          'border-width': '2px',
          'border-color': '#60a5fa'
        }
      },
      {
        selector: 'node[type="constant"]',
        style: { 'background-color': '#f59e0b', 'border-color': '#fbbf24' }
      },
      {
        selector: 'node[type="mirror"]',
        style: { 'background-color': '#10b981', 'border-color': '#34d399' }
      },
      {
        selector: 'node[type="latch"]',
        style: { 'background-color': '#8b5cf6', 'border-color': '#a78bfa' }
      },
      {
        selector: 'edge',
        style: {
          'width': 2,
          'line-color': '#475569',
          'target-arrow-color': '#475569',
          'target-arrow-shape': 'triangle',
          'curve-style': 'bezier',
          'label': 'data(label)',
          'font-size': '10px',
          'color': '#94a3b8'
        }
      }
    ],
    layout: {
      name: 'cose',
      animate: true
    }
  });

  cy.on('tap', 'node', function(evt){
    const node = evt.target;
    document.getElementById('node-details').innerHTML = `
      <h3>${node.data('label')}</h3>
      <p><b>Type:</b> ${node.data('type')}</p>
      <p>${node.data('desc')}</p>
    `;
  });
});
