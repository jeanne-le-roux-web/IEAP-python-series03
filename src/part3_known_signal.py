# Part 3 - Section 3: known signal and frequency
# %%
import numpy as np
import matplotlib.pyplot as plt
 
# functions from parts 1 and 2
from part1_zero_crossings import find_zero_crossings, plot_signal, plot_zero_crossings
from part2_extrema import plot_local_maxima, plot_local_minima
 # %% [markdown]
# ## 3. Analyze a known signal
# A reusable function to generate a sine wave from its amplitude, frequency and phase,
# so both components of the signal are built the same way.
# %%
def sinusoid(t: np.ndarray, amplitude: float, frequency: float, phase: float = 0.0):
    """
    Generate a sine wave.
 
    Parameters
    ----------
    t : np.ndarray
        Time values, in seconds.
    amplitude : float
        Amplitude of the wave.
    frequency : float
        Frequency of the wave, in Hz.
    phase : float, optional
        Phase shift, in radians, 0 by default.
 
    Returns
    -------
    np.ndarray
        Values of the sine wave at each time t.
    """
    return amplitude * np.sin(2 * np.pi * frequency * t + phase)
 
 
# %% [markdown]
# The signal is the sum of two sine waves: a 2 Hz wave of amplitude 1 and a 1 Hz wave
# of amplitude 2 with a phase of 1 rad, sampled at 100 Hz during 2 seconds.
# %%
def create_signal(duration: float = 2.0, sampling_frequency: float = 100.0):
    """
    Create the homework signal and its two components.
 
    Parameters
    ----------
    duration : float, optional
        Duration of the signal, in seconds, 2 by default.
    sampling_frequency : float, optional
        Sampling frequency, in Hz, 100 by default.
 
    Returns
    -------
    t : np.ndarray
        Time values, in seconds.
    s1 : np.ndarray
        2 Hz sine wave, amplitude 1.
    s2 : np.ndarray
        1 Hz sine wave, amplitude 2, phase 1 rad.
    s : np.ndarray
        Sum of s1 and s2.
    """
    # one sample every 1/sampling_frequency seconds
    t = np.arange(0, duration, 1 / sampling_frequency)
    s1 = sinusoid(t, amplitude=1, frequency=2)
    s2 = sinusoid(t, amplitude=2, frequency=1, phase=1)
    s = s1 + s2
    return t, s1, s2, s
 
 
# %% [markdown]
# The signal is plotted as dots only, to show that it is sampled, as in the homework figure.
# %%
def display_sampled_signal(t: np.ndarray, s: np.ndarray, sampling_frequency: float):
    """
    Create a new figure with the sampled signal as dots, as in the homework, then show it.
 
    Parameters
    ----------
    t : np.ndarray
        Time values, in seconds.
    s : np.ndarray
        Signal values.
    sampling_frequency : float
        Sampling frequency, in Hz, shown in the title.
 
    Returns
    -------
    None. Shows the figure with plt.show().
    """
    plt.figure()
    plt.axhline(y=0, color="black")
    plt.plot(t, s, ".", color="steelblue")
    plt.title(f"Sampling at {sampling_frequency}Hz")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude (mm)")
    plt.grid(True)
    plt.show()
 
 