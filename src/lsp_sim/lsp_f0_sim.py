import numpy as np
from scipy.linalg import sqrtm

def lsp_f0_sim(
    num_sim: int,
    f0: float,
    a_q: float,
    b_q: float,
    c_q: float,
    c_r: float,
    sigma_square: float,
    N: int,
    time: np.ndarray
):
    """
    Simulate a locally stationary process with center frequency f0.

    Parameters
    ----------
    num_sim : int         Number of simulated trajectories
    f0 : float            Centre frequency
    a_q, b_q, c_q, c_r : float   Model parameters
    sigma_square : float  Constant noise level
    N : int               Length of each trajectory
    time : array_like     Time vector of length N

    Returns
    -------
    X : (N, num_sim)      Base-band realizations
    X_freq : (N, num_sim) Frequency-modulated realizations
    C : (N, N)            Covariance matrix (base-band)
    C_freq : (N, N)       Covariance matrix with frequency modulation
    R : (N, N)            Stationary part of covariance
    R_freq : (N, N)       Frequency-modulated stationary part
    Q : (N, N)            Time-varying part of covariance
    """
    t = np.array(time).reshape(-1)
    s = t[:, None]

    tau_R = t[None, :] - s
    tau_Q = (t[None, :] + s) / 2

    R = np.exp(-(c_r / 8.0) * (tau_R ** 2))
    R_freq = R * np.cos(2 * np.pi * f0 * tau_R)
    Q = sigma_square + a_q * np.exp(-(c_q / 2.0) * ((tau_Q - b_q) ** 2))

    C = R * Q
    C_freq = R_freq * Q

    Noise = np.random.randn(N, num_sim)

    c1 = sqrtm(C)
    c2 = sqrtm(C_freq)

    X = np.real(c1) @ Noise
    X_freq = np.real(c2) @ Noise

    return X, X_freq, C, C_freq, R, R_freq, Q
