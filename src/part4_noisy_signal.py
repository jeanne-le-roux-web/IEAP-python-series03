
# Part 4 - Noisy Signal and Filtering

# %%
import numpy as np
import matplotlib.pyplot as plt

from part3_known_signal import create_signal

from part1_zero_crossings import (
    plot_signal,
    plot_zero_crossings
)

from part2_extrema import (
    plot_local_maxima,
    plot_local_minima
)

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

# %% [markdown]
# ### Plot the noisy signal


# %%
def display_noisy_signal(
    t: np.ndarray,
    noisy_signal: np.ndarray
):
    """
    Plot the signal containing noise.

    Parameters
    ----------
    t : np.ndarray
        Time values, in seconds.
    noisy_signal : np.ndarray
        Signal containing noise.

    Returns
    -------
    None. Shows the figure.
    """

    plt.figure(figsize=(10, 5))

    plt.axhline(
        y=0,
        color="black"
    )

    plt.plot(
        t,
        noisy_signal,
        ".-",
        markersize=3,
        linewidth=0.25,
        color="steelblue",
        label="Noisy signal"
    )

    plt.title("Noisy Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.show()
    # %% [markdown]
# ### Compare the original and noisy signals


# %%
def display_amplitude_comparison(
    t: np.ndarray,
    original_signal: np.ndarray,
    noisy_signal: np.ndarray
):
    """
    Compare the original signal with the noisy signal.

    Parameters
    ----------
    t : np.ndarray
        Time values, in seconds.
    original_signal : np.ndarray
        Original signal.
    noisy_signal : np.ndarray
        Signal containing noise.

    Returns
    -------
    None. Shows the figure.
    """

    plt.figure(figsize=(10, 5))

    plt.plot(
        t,
        original_signal,
        color="blue",
        linewidth=1.5,
        label="Original signal"
    )

    plt.plot(
        t,
        noisy_signal,
        color="orange",
        linewidth=0.8,
        label="Noisy signal"
    )

    plt.title("Amplitude Comparison: Original vs Noisy Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.show()

# %% [markdown]
# ### Generate and display the noisy signal
#
# Calculate the peak-to-peak amplitude of the original signal.
# Set the noise amplitude to 20% of this value.


# %%
if __name__ == "__main__":

    # Generate the original signal using Part 3
    sampling_frequency = 100.0

    t, s1, s2, s = create_signal(
        sampling_frequency=sampling_frequency
    )

    # Calculate the peak-to-peak amplitude
    signal_peak_to_peak_amplitude = np.ptp(s)

    # Set noise amplitude to 20% of signal amplitude
    noise_amplitude = 0.2 * signal_peak_to_peak_amplitude

    print(
        "Signal peak-to-peak amplitude:",
        signal_peak_to_peak_amplitude
    )

    print(
        "Noise amplitude:",
        noise_amplitude
    )

    # Generate noisy signal and noise
    noisy_signal, noise = create_noisy_signal(
        t,
        s,
        noise_amplitude
    )

    # Plot white noise
    display_noise(t, noise)

    # Plot noisy signal
    display_noisy_signal(t, noisy_signal)

    # Compare original and noisy signals
    display_amplitude_comparison(
        t,
        s,
        noisy_signal
    )

# %%
