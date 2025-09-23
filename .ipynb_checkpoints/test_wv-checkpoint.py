import numpy as np
import matplotlib.pyplot as plt


# Parameters
a_q = 500
b_q = 0.2
c_q = 800
c_r = 15000
noise = 0
dataN = 256

T0 = 0
Tf = 0.5
delta_t = abs(Tf - T0) / (dataN - 1)
time_vec = T0 + np.arange(dataN) * delta_t

fs = 512
f0 = 25   # Hz
nfft = 512

WVshift, TI, FI, WV0 = WVshifted_LSP(noise, a_q, b_q, c_q, c_r, dataN, f0, fs, nfft)

# Check peak freq and time
# If WVshift is (time, freq): use WVshift.T in sums
peak_freq_bin = np.argmax(np.abs(WVshift).T.sum(axis=1))
peak_time_bin = np.argmax(np.abs(WVshift).sum(axis=1))
print("Peak ~ f =", FI[peak_freq_bin], "Hz,  t =", TI[peak_time_bin], "s")


# Quick visualization
plt.figure(figsize=(8,6))
plt.imshow(np.abs(WVshift).T, aspect='auto',
           extent=[TI[0], TI[-1], FI[0], FI[-1]],
           origin='lower')
plt.colorbar(label='|WVshift|')
plt.xlabel("Time (s)")
plt.ylabel("Frequency (Hz)")
plt.title("Shifted Wigner-Ville Spectrum")

plt.show()
