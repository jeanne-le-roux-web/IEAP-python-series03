# Part 2 - Section 2.3: local maxima and minima

# %%
import numpy as np
import matplotlib.pyplot as plt

# functions and reference signal from part 1
from part1_zero_crossings import find_zero_crossings, plot_signal, plot_remarkable_points, index, signal

# %% [markdown]
# ### 2.3. Create new functions to find the local maxima and minima

# %% [markdown]
# Local maxima and minima are the zero crossings of the first derivative: at a maximum
# the slope goes from positive to negative, at a minimum from negative to positive.
# We approximate the derivative with `np.diff` and reuse `find_zero_crossings` from part 1.

# %%
def find_local_extrema(s: np.ndarray):
    """
    Find the local maxima and minima of a 1D signal.

    The derivative is approximated by np.diff(s). A negative zero crossing
    of the derivative is a local maximum, a positive one is a local minimum.
    If the extremum is a plateau (several consecutive samples with the same
    value), only the last sample of the plateau is returned.

    Parameters
    ----------
    s : np.ndarray (or list)
        1D signal.

    Returns
    -------
    i_local_max : np.ndarray
        Indices of the local maxima in s.
    i_local_min : np.ndarray
        Indices of the local minima in s.
    """
    s = np.asarray(s)
    # approximate first derivative: d[k] = s[k+1] - s[k]
    derivative = np.diff(s)
    # a sign change of the derivative between k and k+1 means an extremum at sample k+1
    i_cross_pos, i_cross_neg = find_zero_crossings(derivative)
    # shift by 1 to get indices in the original signal
    i_local_max = i_cross_neg + 1
    i_local_min = i_cross_pos + 1
    return i_local_max, i_local_min

# %% [markdown]
# The tests below check the function on the reference signal and on simple cases with a
# known answer.

# %%
def test_find_local_extrema():
    """
    Unit tests for find_local_extrema.

    Raises an AssertionError as soon as one test fails.
    """
    # reference signal: maxima at 2 and 7, minimum at 5
    i_max, i_min = find_local_extrema(np.array([-1, 1, 2, 1, 0, -1, 1, 2, 1, -2]))
    assert np.array_equal(i_max, np.array([2, 7]))
    assert np.array_equal(i_min, np.array([5]))

    # single peak
    i_max, i_min = find_local_extrema(np.array([0, 1, 0]))
    assert np.array_equal(i_max, np.array([1]))
    assert np.array_equal(i_min, np.array([]))

    # single valley
    i_max, i_min = find_local_extrema(np.array([0, -1, 0]))
    assert np.array_equal(i_max, np.array([]))
    assert np.array_equal(i_min, np.array([1]))

    # monotonic signal: no extremum
    i_max, i_min = find_local_extrema(np.array([1, 2, 3]))
    assert np.array_equal(i_max, np.array([]))
    assert np.array_equal(i_min, np.array([]))

        # flat top: only the last sample of the plateau is returned
    i_max, i_min = find_local_extrema(np.array([0, 1, 1, 0]))
    assert np.array_equal(i_max, np.array([2]))
    assert np.array_equal(i_min, np.array([]))

    # flat valley: only the last sample of the plateau is returned
    i_max, i_min = find_local_extrema(np.array([1, 0, 0, 1]))
    assert np.array_equal(i_max, np.array([]))
    assert np.array_equal(i_min, np.array([2]))


# Testing the function (only when this file is run, not when it is imported)
if __name__ == "__main__":
    try:
        test_find_local_extrema()
        print("All tests passed.")
    except AssertionError:
        raise  # propagate the error

# %% [markdown]
# The plotting functions follow the same naming conventions as before: `plot_` functions
# draw without showing, the `display_` function shows the final figure.

# %%
def plot_local_maxima(i: np.ndarray, s: np.ndarray):
    """
    Find the local maxima of a signal and mark them with red stars.

    Parameters
    ----------
    i : np.ndarray
        Time or index values of the signal.
    s : np.ndarray
        Signal values.

    Returns
    -------
    None. Draws on the current figure without showing it.
    """
    i_max, _ = find_local_extrema(s)
    plot_remarkable_points(i[i_max], s[i_max], "*r", "local maxima")


def plot_local_minima(i: np.ndarray, s: np.ndarray):
    """
    Find the local minima of a signal and mark them with purple stars.

    Parameters
    ----------
    i : np.ndarray
        Time or index values of the signal.
    s : np.ndarray
        Signal values.

    Returns
    -------
    None. Draws on the current figure without showing it.
    """
    _, i_min = find_local_extrema(s)
    plot_remarkable_points(i[i_min], s[i_min], "*m", "local minima")


def display_signal_and_extrema(i: np.ndarray, s: np.ndarray):
    """
    Create a new figure with the signal and its local extrema, then show it.

    Parameters
    ----------
    i : np.ndarray
        Time or index values of the signal.
    s : np.ndarray
        Signal values.

    Returns
    -------
    None. Shows the figure with plt.show().
    """
    plt.figure()
    plot_signal(i, s)
    plot_local_maxima(i, s)
    plot_local_minima(i, s)
    plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.grid(True)
    plt.show()


# Example usage (only when this file is run, not when it is imported)
if __name__ == "__main__":
    display_signal_and_extrema(index, signal)