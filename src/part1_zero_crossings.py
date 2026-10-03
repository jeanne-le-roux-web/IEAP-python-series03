# Part 1 - Sections 2.1 and 2.2: zero crossings (docstrings, comments, tests)

# %%
import numpy as np
import matplotlib.pyplot as plt

# reference signal for the tests
index = np.arange(10)
signal = np.array([-1, 1, 2, 1, 0, -1, 1, 2, 1, -2])

# %% [markdown]
# ## 2. Create functions to find and plot remarkable points
# ### 2.1. Functions to find zero crossings and to plot them

# %%
def find_zero_crossings_no_zeros(signs: np.ndarray):
    """Find zero crossings in a sign array without zeros"""
    diff = np.diff(signs)
    i_cross_pos = np.where(diff > 0)[0]
    i_cross_neg = np.where(diff < 0)[0]
    return i_cross_pos, i_cross_neg


def propagate_signs_over_zeros(signs: np.ndarray):
    """Propagate non-zero signs over zero positions in the sign array."""

    signs_no_zeros = signs.copy()

    mask = signs_no_zeros != 0
    idx = np.where(mask, np.arange(len(signs_no_zeros)), 0)
    idx = np.maximum.accumulate(idx)
    signs_no_zeros = signs_no_zeros[idx]

    if signs_no_zeros[0] == 0:
        i_first_nonzero = np.where(signs != 0)[0]
        if len(i_first_nonzero) > 0:
            signs_no_zeros[: i_first_nonzero[0]] = signs[i_first_nonzero[0]]

    return signs_no_zeros


def find_zero_crossings(s: np.ndarray):
    """Find zero crossings in a 1D signal array."""

    s = np.asarray(s)
    if s.ndim != 1:
        raise ValueError("Input must be a 1D array")

    signs = np.sign(s).astype(int)
    i_zeros = np.where(signs == 0)[0]
    if i_zeros.size > 0:
        signs_no_zeros = propagate_signs_over_zeros(signs)
    else:
        signs_no_zeros = signs

    return find_zero_crossings_no_zeros(signs_no_zeros)


# %%
def test_find_zero_crossings():
    """Unit tests for find_zero_crossings function."""
    s = np.array([-1, 1, -1, 1, -1])
    # expected     +  -   +  -   +
    i_pos, i_neg = find_zero_crossings(s)
    assert np.array_equal(i_pos, np.array([0, 2]))
    assert np.array_equal(i_neg, np.array([1, 3]))

    s = np.array([-1, 0, 0, 1, 0, -1])
    # expected     -     +     -
    i_pos, i_neg = find_zero_crossings(s)
    assert np.array_equal(i_pos, np.array([2]))
    assert np.array_equal(i_neg, np.array([4]))

    s = np.array([0, 0, 0, 1, 0, 0])
    # expected    no crossings
    i_pos, i_neg = find_zero_crossings(s)
    assert np.array_equal(i_pos, np.array([]))
    assert np.array_equal(i_neg, np.array([]))

    s = np.array([0, 0, 1, 0, -1, 0])
    # expected             -
    i_pos, i_neg = find_zero_crossings(s)
    assert np.array_equal(i_pos, np.array([]))
    assert np.array_equal(i_neg, np.array([3]))

    s = np.array([0, 1, 0, 0, -1, 0])
    # expected             -
    i_pos, i_neg = find_zero_crossings(s)
    assert np.array_equal(i_pos, np.array([]))
    assert np.array_equal(i_neg, np.array([3]))

    s = np.array([1, 0, 0, -1, 0, 0])
    # expected          -
    i_pos, i_neg = find_zero_crossings(s)
    assert np.array_equal(i_pos, np.array([]))
    assert np.array_equal(i_neg, np.array([2]))


# Testing the function
try:
    test_find_zero_crossings()
    print("All tests passed.")
except AssertionError:
    raise  # propagate the error



# %%
def plot_signal(i: np.ndarray, s: np.ndarray, color: str = "blue"):
    """Plot the signal as function of time/index with grid and zero line"""
    plt.axhline(y=0, color="gray", linestyle="-")  # before to be under the signal
    plt.plot(i, s, ".-", markersize=5, linewidth=0.25, color=color, label="signal")
    plt.ylabel("signal")
    plt.xlabel("index")


def plot_remarkable_points(t: np.ndarray, s: np.ndarray, format: str, label: str):
    """Plot remarkable points on a signal with format and label"""
    plt.plot(t, s, format, markersize=10, label=label)


def plot_positive_zero_crossings(i: np.ndarray, s: np.ndarray):
    """Plot positive zero crossings on a signal"""
    i_pos, _ = find_zero_crossings(s)
    plot_remarkable_points(i[i_pos], s[i_pos], "^r", "positive zero crossings")


def plot_negative_zero_crossings(i: np.ndarray, s: np.ndarray):
    """Plot negative zero crossings on a signal"""
    _, i_neg = find_zero_crossings(s)
    plot_remarkable_points(i[i_neg], s[i_neg], "vy", "negative zero crossings")


def plot_zero_crossings(i: np.ndarray, s: np.ndarray):
    """Plot all zero crossings on a signal"""
    plot_positive_zero_crossings(i, s)
    plot_negative_zero_crossings(i, s)


def display_signal_and_crossings(i: np.ndarray, s: np.ndarray):
    """Plot signal and zero crossings with legend outside the plot and grid"""
    plt.figure()
    plot_signal(i, s)
    plot_positive_zero_crossings(i, s)
    plot_negative_zero_crossings(i, s)
    # NOTE: legend outside does not work well with %matplotlib widget
    plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.grid(True)
    plt.show()


# Example usage
display_signal_and_crossings(index, signal)


# %% [markdown]
# ### 2.2. Explain and improve the previous code

# %% [markdown]
# Same code as in 2.1, with complete docstrings (purpose, inputs, outputs) and comments
# explaining each line that is not straightforward, in particular the trick used in
# `propagate_signs_over_zeros` to replace the zeros by the last non zero sign.

# %%
def find_zero_crossings_no_zeros(signs: np.ndarray):
    """
    Find positive and negative zero crossings in a sign array that contains no zeros.

    Parameters
    ----------
    signs : np.ndarray
        1D array containing only -1 and +1 values.

    Returns
    -------
    i_cross_pos : np.ndarray
        Indices i where the sign goes from -1 to +1 between i and i+1.
    i_cross_neg : np.ndarray
        Indices i where the sign goes from +1 to -1 between i and i+1.
    """
    # difference between consecutive signs: +2 (from -1 to +1), -2 (from +1 to -1), 0 (no change)
    diff = np.diff(signs)
    # np.where returns a tuple, [0] extracts the array of indices
    i_cross_pos = np.where(diff > 0)[0]
    i_cross_neg = np.where(diff < 0)[0]
    return i_cross_pos, i_cross_neg


def propagate_signs_over_zeros(signs: np.ndarray):
    """
    Replace each zero in a sign array by the last non zero sign before it.

    Leading zeros (at the start, with no previous non zero sign) are replaced
    by the first non zero sign that follows them.

    Parameters
    ----------
    signs : np.ndarray
        1D array of -1, 0 and +1 values.

    Returns
    -------
    signs_no_zeros : np.ndarray
        Array of the same length with zeros replaced. If the input contains
        only zeros, it is returned unchanged.
    """
    # work on a copy to keep the original array unchanged
    signs_no_zeros = signs.copy()

    # --- forward fill: replace zeros by the last non zero sign before them ---
    # True where the sign is not zero
    mask = signs_no_zeros != 0
    # each position keeps its own index if its sign is non zero, otherwise 0
    idx = np.where(mask, np.arange(len(signs_no_zeros)), 0)
    # running maximum: each position now holds the index of the last non zero sign so far
    idx = np.maximum.accumulate(idx)
    # pick the sign at that index for every position
    signs_no_zeros = signs_no_zeros[idx]

    # --- backward fill: leading zeros have no previous non zero sign ---
    if signs_no_zeros[0] == 0:
        # indices of all non zero signs in the original array
        i_first_nonzero = np.where(signs != 0)[0]
        # only possible if the signal is not entirely zero
        if len(i_first_nonzero) > 0:
            # fill the leading zeros with the first non zero sign
            signs_no_zeros[: i_first_nonzero[0]] = signs[i_first_nonzero[0]]

    return signs_no_zeros


def find_zero_crossings(s: np.ndarray):
    """
    Find positive and negative zero crossings in a 1D signal.

    Samples exactly equal to zero are handled by replacing them with the
    last non zero sign, so a crossing through zero is detected only once.

    Parameters
    ----------
    s : np.ndarray (or list)
        1D signal.

    Returns
    -------
    i_cross_pos : np.ndarray
        Indices i of positive zero crossings (sign change between i and i+1).
    i_cross_neg : np.ndarray
        Indices i of negative zero crossings (sign change between i and i+1).

    Raises
    ------
    ValueError
        If the input is not a 1D array.
    """
    # accept lists as well as numpy arrays
    s = np.asarray(s)
    # the algorithm only works on 1D signals
    if s.ndim != 1:
        raise ValueError("Input must be a 1D array")

    # sign of each sample: -1, 0 or +1, as integers
    signs = np.sign(s).astype(int)
    # zeros would hide the sign changes, so replace them before detection
    i_zeros = np.where(signs == 0)[0]
    if i_zeros.size > 0:
        signs_no_zeros = propagate_signs_over_zeros(signs)
    else:
        signs_no_zeros = signs

    return find_zero_crossings_no_zeros(signs_no_zeros)


# %% [markdown]
# The unit tests check that `find_zero_crossings` returns the expected result on small
# signals whose answer is known in advance. They are useful for three reasons:
#
# 1. They prove that the function works on the tricky cases (zeros in the middle, at the
#    start, at the end, signal touching zero without crossing it).
# 2. They detect regressions: each time we modify the code (for example when we added
#    comments and docstrings above), running the tests again shows immediately if
#    something is broken.
# 3. They document the expected behaviour: reading the test cases shows how the function
#    handles each situation.
#
# The additional test cases below cover the scenarios that were not tested yet: signals
# with no crossing at all, signals touching zero without crossing, trailing zeros, single
# sample and empty signals, float values, list inputs, and invalid 2D inputs.

# %%
def test_find_zero_crossings():
    """
    Unit tests for find_zero_crossings.

    Each test builds a small signal with a known answer and checks that the
    function returns the expected indices of positive and negative crossings.
    Raises an AssertionError as soon as one test fails.
    """
    # ===== original test cases =====
    s = np.array([-1, 1, -1, 1, -1])
    # expected     +  -   +  -   +
    i_pos, i_neg = find_zero_crossings(s)
    assert np.array_equal(i_pos, np.array([0, 2]))
    assert np.array_equal(i_neg, np.array([1, 3]))

    s = np.array([-1, 0, 0, 1, 0, -1])
    # expected     -     +     -
    i_pos, i_neg = find_zero_crossings(s)
    assert np.array_equal(i_pos, np.array([2]))
    assert np.array_equal(i_neg, np.array([4]))

    s = np.array([0, 0, 0, 1, 0, 0])
    # expected    no crossings
    i_pos, i_neg = find_zero_crossings(s)
    assert np.array_equal(i_pos, np.array([]))
    assert np.array_equal(i_neg, np.array([]))

    s = np.array([0, 0, 1, 0, -1, 0])
    # expected             -
    i_pos, i_neg = find_zero_crossings(s)
    assert np.array_equal(i_pos, np.array([]))
    assert np.array_equal(i_neg, np.array([3]))

    s = np.array([0, 1, 0, 0, -1, 0])
    # expected             -
    i_pos, i_neg = find_zero_crossings(s)
    assert np.array_equal(i_pos, np.array([]))
    assert np.array_equal(i_neg, np.array([3]))

    s = np.array([1, 0, 0, -1, 0, 0])
    # expected          -
    i_pos, i_neg = find_zero_crossings(s)
    assert np.array_equal(i_pos, np.array([]))
    assert np.array_equal(i_neg, np.array([2]))

    # ===== additional test cases =====
    # always positive: no crossing
    i_pos, i_neg = find_zero_crossings(np.array([1, 2, 3]))
    assert np.array_equal(i_pos, np.array([]))
    assert np.array_equal(i_neg, np.array([]))

    # always negative: no crossing
    i_pos, i_neg = find_zero_crossings(np.array([-1, -2, -3]))
    assert np.array_equal(i_pos, np.array([]))
    assert np.array_equal(i_neg, np.array([]))

    # only zeros: no crossing
    i_pos, i_neg = find_zero_crossings(np.array([0, 0, 0]))
    assert np.array_equal(i_pos, np.array([]))
    assert np.array_equal(i_neg, np.array([]))

    # touches zero from above without crossing
    i_pos, i_neg = find_zero_crossings(np.array([1, 0, 1]))
    assert np.array_equal(i_pos, np.array([]))
    assert np.array_equal(i_neg, np.array([]))

    # touches zero from below without crossing
    i_pos, i_neg = find_zero_crossings(np.array([-1, 0, -1]))
    assert np.array_equal(i_pos, np.array([]))
    assert np.array_equal(i_neg, np.array([]))

    # trailing zeros after a crossing
    i_pos, i_neg = find_zero_crossings(np.array([1, -1, 0, 0]))
    assert np.array_equal(i_pos, np.array([]))
    assert np.array_equal(i_neg, np.array([0]))

    # single sample: no crossing possible
    i_pos, i_neg = find_zero_crossings(np.array([5]))
    assert np.array_equal(i_pos, np.array([]))
    assert np.array_equal(i_neg, np.array([]))

    # empty signal: no crossing
    i_pos, i_neg = find_zero_crossings(np.array([]))
    assert np.array_equal(i_pos, np.array([]))
    assert np.array_equal(i_neg, np.array([]))

    # float values
    i_pos, i_neg = find_zero_crossings(np.array([-0.5, 0.2, -0.1]))
    assert np.array_equal(i_pos, np.array([0]))
    assert np.array_equal(i_neg, np.array([1]))

    # list input instead of numpy array
    i_pos, i_neg = find_zero_crossings([-1, 1])
    assert np.array_equal(i_pos, np.array([0]))
    assert np.array_equal(i_neg, np.array([]))

    # 2D input must raise a ValueError
    raised = False
    try:
        find_zero_crossings(np.array([[1, -1], [-1, 1]]))
    except ValueError:
        raised = True
    assert raised


# Testing the function
try:
    test_find_zero_crossings()
    print("All tests passed.")
except AssertionError:
    raise  # propagate the error



#  %% [markdown]
#Improved plotting functions

#Same code as in 2.1, with complete docstrings. The code itself is unchanged, so the figure below must be identical to the one in 2.1.


# %%
def plot_signal(i: np.ndarray, s: np.ndarray, color: str = "blue"):
    """
    Plot a signal as a function of time or index, with a horizontal zero line.

    Parameters
    ----------
    i : np.ndarray
        Time or index values (x axis).
    s : np.ndarray
        Signal values (y axis).
    color : str, optional
        Color of the signal, "blue" by default.

    Returns
    -------
    None. Draws on the current figure without showing it.
    """
    plt.axhline(y=0, color="gray", linestyle="-")  # before to be under the signal
    plt.plot(i, s, ".-", markersize=5, linewidth=0.25, color=color, label="signal")
    plt.ylabel("signal")
    plt.xlabel("index")


def plot_remarkable_points(t: np.ndarray, s: np.ndarray, format: str, label: str):
    """
    Plot markers at given positions on the current figure.

    Parameters
    ----------
    t : np.ndarray
        Time or index values of the points to mark.
    s : np.ndarray
        Signal values of the points to mark.
    format : str
        Matplotlib marker format, for example "^r" for red upward triangles.
    label : str
        Label shown in the legend.

    Returns
    -------
    None. Draws on the current figure without showing it.
    """
    plt.plot(t, s, format, markersize=10, label=label)


def plot_positive_zero_crossings(i: np.ndarray, s: np.ndarray):
    """
    Find the positive zero crossings of a signal and mark them with red upward triangles.

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
    i_pos, _ = find_zero_crossings(s)
    plot_remarkable_points(i[i_pos], s[i_pos], "^r", "positive zero crossings")


def plot_negative_zero_crossings(i: np.ndarray, s: np.ndarray):
    """
    Find the negative zero crossings of a signal and mark them with yellow downward triangles.

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
    _, i_neg = find_zero_crossings(s)
    plot_remarkable_points(i[i_neg], s[i_neg], "vy", "negative zero crossings")


def plot_zero_crossings(i: np.ndarray, s: np.ndarray):
    """
    Mark both positive and negative zero crossings of a signal.

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
    plot_positive_zero_crossings(i, s)
    plot_negative_zero_crossings(i, s)


def display_signal_and_crossings(i: np.ndarray, s: np.ndarray):
    """
    Create a new figure with the signal and its zero crossings, then show it.

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
    plot_positive_zero_crossings(i, s)
    plot_negative_zero_crossings(i, s)
    # NOTE: legend outside does not work well with %matplotlib widget
    plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.grid(True)
    plt.show()


# Example usage
display_signal_and_crossings(index, signal)

# %%
