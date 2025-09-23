# lsp-sim

**Locally Stationary Process Simulation in Python**

This package provides tools to simulate *locally stationary processes (LSPs)* following Silverman’s definition.  
It includes the function `lsp_f0_sim` for generating realizations with time-varying covariance.


---

## Features
- Simulate multiple realizations of an LSP.  
- Flexible covariance structure: stationary correlation part $r(\tau)$ and time-varying power part $q(\eta)$.  
- In this implementation, $q(\eta)$ and $r(\tau)$ are chosen as Gaussian functions.  
- Jupyter notebook demo included for exploring parameter effects.  
- Reproducible simulations using fixed random seeds.  

---

## Installation

Clone the repository and install in editable mode (so changes are reflected immediately):

```bash
git clone https://github.com/RacheleAnderson/lsp-sim.git
cd lsp-sim
uv pip install -e .
```
---

## Jupyter Demo

Launch the included notebook to see comparisons across parameter sets:

```bash
uv run jupyter notebook notebooks/demo_lsp_sim.ipynb
```

The demo visualizes:

- Several simulated realizations
- Covariance matrices for different parameter configurations
- Different behaviors of the realizations when changing the parameters of the chosen Gaussian-shaped $q(\eta)$ and $r(\tau)$ functions

## Background 

The model is presented in the research paper

Anderson, R., Sandsten, M. Time-frequency feature extraction for classification of episodic memory. EURASIP J. Adv. Signal Process. 2020, 19 (2020).

available online (Open Access) at: https://doi.org/10.1186/s13634-020-00681-8

## License  
MIT License — see [LICENSE](LICENSE) for details.


