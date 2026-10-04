
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