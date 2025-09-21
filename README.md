# lsp-sim

**Locally Stationary Process Simulation in Python**

This package provides tools to simulate *locally stationary processes (LSPs)* following Silverman’s definition.  
It includes the function `lsp_f0_sim` for generating realizations with time-varying covariance.


---

## Features
- Simulate multiple realizations of an LSP.  
- Flexible covariance structure: stationary correlation part $R(\tau)$ and time-varying power part $Q(\eta)$.  
- In this implementation, $Q(\eta)$ and $R(\tau)$ are  chosen as Gaussian functions.  
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
- Different behaviors of the realizations when changing the parameters of the chosen Gaussian-shaped $Q(\eta)$ and $R(\tau)$ functions

## Background 

The model is presented in the research paper

Anderson R., Sandsten M., "Inference for time-varying signals using Locally Stationary Processes", Journal of Computational and Applied Mathematics, Volume 347, Pages 24-35, 2019.

available online at: https://doi.org/10.1016/j.cam.2018.07.046

## License  
MIT License — see [LICENSE](LICENSE) for details.


