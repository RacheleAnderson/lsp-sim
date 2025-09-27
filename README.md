# lsp-sim

**Locally Stationary Process Simulation in Python**

This package provides tools to simulate *locally stationary processes (LSPs)* in Silverman’s sense with a flexible covariance structure: stationary correlation part $r(\tau)$ and time-varying power part $q(\eta)$, both chosen as Gaussian functions. 

It includes the functions:

-`lsp_f0_sim` for simulating LSP realizations

-`wv_lsp` for calculating the Wigner-Ville distribution of the LSP


## Jupyter Demo

Use the simple Jupyter notebook demo `demo_lsp_sim.ipynb` https://github.com/RacheleAnderson/lsp-sim/blob/main/notebooks/demo_lsp_sim.ipynb
for exploring parameter effects.  
Reproducible simulations can be obtained by fixing random seeds.  
Full source code and notebook demo are available on GitHub https://github.com/RacheleAnderson/lsp-sim/

The demo visualizes:

- Simulated realizations showing different behaviors of the realizations when changing the parameters (3 cases)
- Covariance matrices for the 3 cases of different parameter configurations
- Wigner-Ville distribution for the 3 cases of different parameter configurations

## Background 

The model is presented in the research paper

Anderson, R., Sandsten, M. Time-frequency feature extraction for classification of episodic memory. EURASIP J. Adv. Signal Process. 2020, 19 (2020).

available online (Open Access) at: https://doi.org/10.1186/s13634-020-00681-8

Previous Matlab code is available for repeating the study, see https://github.com/RacheleAnderson/lsp-time-frequency. 

This Python package is a simpler version with the limited scope of simulating LSP realizations according to the model.  

## License  
MIT License — see [LICENSE](LICENSE) for details.


