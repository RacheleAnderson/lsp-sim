import numpy as np

def wvshifted_lsp(noise_level, a_q, b_q, c_q, c_r, dataN, f0, fs, nfft):
    """
    Compute Wigner-Ville spectrum and shift it to f0 centre frequency.

    Parameters
    ----------
    noise_level : float
        Baseline noise level.
    a_q, b_q, c_q : floats
        Parameters of q(x).
    c_r : float
        Parameter of r(x).
    dataN : int
        Number of data points.
    f0 : float
        Centre frequency.
    fs : float
        Sampling frequency.
    nfft : int
        FFT size.

    Returns
    -------
    WVshift : ndarray
        Shifted Wigner-Ville spectrum.
    TI : ndarray
        Time indices.
    FI : ndarray
        Frequency indices.
    WV0 : ndarray
        Original Wigner-Ville spectrum.
    """

    # time and frequency axes
    tl = np.arange(dataN) / fs                       # [dataN,]
    f = np.arange(-nfft//2, nfft//2) * fs / nfft     # [nfft,]

    # build theta and tau grids
    theta = 2 * np.pi * f[:, np.newaxis]             # shape (nfft,1)
    tau = tl[np.newaxis, :]                          # shape (1,dataN)

    # Fourier transform of r
    Fr = 2 * np.sqrt(2*np.pi / c_r) * np.exp(-(2/c_r) * theta**2)  # [nfft,1]

    # q(x)
    q = noise_level + a_q * np.exp(-c_q/2 * (tau - b_q)**2)        # [1,dataN]

    # Wigner-Ville spectrum
    WV0 = Fr @ q   # matrix multiply → shape (nfft,dataN)

    # shift WV to match frequency in the signal
    d = f0 / fs
    L = int(np.floor(d * nfft))   # centre freq row

    start = nfft//2 - L
    stop = nfft//2 + (nfft//2 - L)
    WVshift = WV0[start:start + nfft//2, :]  # shape (nfft/2,dataN)

    # outputs
    TI = tl
    FI = np.arange(nfft//2) / nfft * fs

    WVshift = (WVshift.T) / 2     # transpose + divide by 2

    return WVshift, TI, FI, WV0

