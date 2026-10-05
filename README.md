# IEAP-python-series03

Detection of remarkable points (zero crossings, maxima/minima) and frequency analysis of a signal, with and without noise

## Group and division of tasks

| Member | Sections | File |
|---|---|---|
| Martin Pigeau | 2.2 and 2.3 | `src/part1_zero_crossings.py`, `src/part2_extrema.py` |
| Jeanne Le Roux | 3 and repository | `src/part3_known_signal.py` |
| Tuba | 4 | `src/part4_noisy_signal.py` |

## How to run

```
pip install -r requirements.txt
python src/part1_zero_crossings.py   # zero crossings: unit tests and plot (section 2.2)
python src/part2_extrema.py          # local maxima and minima (section 2.3)
python src/part3_known_signal.py     # known signal and frequency (section 3)
python src/part4_noisy_signal.py     # noisy signal and low-pass filter (section 4)
```

Each file can be run on its own, for example `part3_known_signal.py` shows the plots of section 3 and prints the frequency (1 Hz). The files import each other (part2 and part3 use part1), so they must stay in the same `src/` folder.

## Workflow

The `main` branch is protected: each member works on a personal branch created from the up-to-date `main` and opens a pull request, which another member reviews before the merge.
