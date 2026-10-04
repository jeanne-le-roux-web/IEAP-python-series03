
# Part 4 - Noisy Signal and Filtering

# %%
import numpy as np
import matplotlib.pyplot as plt

from part3_known_signal import create_signal

# %% [markdown]
# ## 4. Redo the analysis with a noisy signal
#
# ### 4.1. Create the noisy signal and plot it
#
# White noise is added to the original signal.
# The noise amplitude is set to 20% of the peak-to-peak
# amplitude of the original signal.
# %%
def create_noisy_signal(
    t: np.ndarray,
    s: np.ndarray,
    noise_amplitude: float
):
    """
    Add random white noise to the original signal.

    Parameters
    ----------
    t : np.ndarray
        Time values, in seconds.
    s : np.ndarray
        Original signal.
    noise_amplitude : float
        Peak-to-peak amplitude of the added noise.

    Returns
    -------
    noisy_signal : np.ndarray
        Original signal with added noise.
    noise : np.ndarray
        Generated noise.
    """

    # Generate random noise
    noise = np.random.uniform(
        -noise_amplitude / 2,
        noise_amplitude / 2,
        size=len(s)
    )

    # Add noise to the original signal
    noisy_signal = s + noise

    return noisy_signal, noise

# %% [markdown]
# ### Plot the white noise

# %%
def display_noise(t: np.ndarray, noise: np.ndarray):
    """
    Plot the generated white noise.

    Parameters
    ----------
    t : np.ndarray
        Time values, in seconds.
    noise : np.ndarray
        Generated noise.

    Returns
    -------
    None. Shows the figure.
    """

    plt.figure(figsize=(10, 5))

    plt.plot(
        t,
        noise,
        ".",
        markersize=5,
        label="Noise"
    )

    plt.title("White Noise")
    plt.xlabel("Time (s)")
    plt.ylabel("Noise amplitude")
    plt.grid(True)
    plt.legend()
    plt.show()

# %%
