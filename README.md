# IEAP Python Series 03

## Detection of Remarkable Points and Frequency Analysis of Signals

The objective of this project is to develop reusable Python functions for detecting remarkable points in signals, analyzing a known signal, estimating its frequency, and studying the effect of noise and filtering on signal analysis.

---

## Group Members & Contributions

Each member worked on a specific part of the assignment using an individual Git branch. After completing and reviewing their work, we merged the contributions into the `main` branch, which contains the final version of the project.

| Branch | Member | Contribution |
|---|---|---|
| `jeanne-part-3` | Jeanne Le Roux | Part 3 – Known signal generation, plotting, and frequency analysis |
| `martin-part-2.2-2.3` | Martin Pigeau | Parts 2.2–2.3 – Improving the zero-crossing approach and implementing local maxima and minima |
| `tuba-part-4` | Tuba Tuba | Part 4 – Noisy signal generation, remarkable points in noisy signals, and Butterworth low-pass filtering |
| `main` | Group | Final integrated version containing the completed work of all group members |

---

## Project Objectives

The main objectives of this assignment are:

- Detect positive and negative zero crossings in a signal.
- Detect local maxima and minima.
- Create reusable functions for signal analysis and visualization.
- Generate and analyze a known signal.
- Estimate signal frequency from zero crossings.
- Add noise to a signal and study its effect.
- Detect remarkable points in a noisy signal.
- Apply a low-pass Butterworth filter to reduce noise.
- Compare the original, noisy, and filtered signals.
- Work collaboratively using Git and GitHub.

---

## Project Structure

```text
IEAP-python-series03/
│
├── src/
│   ├── part1_zero_crossings.py
│   ├── part2_extrema.py
│   ├── part3_known_signal.py
│   └── part4_noisy_signal.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Git and GitHub Workflow

Each member developed their assigned work on their own branch. We made regular commits, pushed our branches to GitHub, and used Pull Requests to review the work before integrating it into the `main` branch.

This workflow allowed us to:

- Work independently on separate parts of the assignment.
- Keep track of each member's contributions.
- Make regular and descriptive commits.
- Review and improve code through Pull Requests.
- Collaborate without overwriting each other's work.

---

## What We Learned

Through this assignment, we learned how to:

- Work with NumPy arrays and numerical signals.
- Use derivatives to identify local extrema.
- Detect zero crossings in discrete signals.
- Create reusable Python functions.
- Estimate signal frequency from sampled data.
- Add and analyze noise.
- Apply digital filtering using SciPy.
- Visualize signal-processing results using Matplotlib.
- Organize a Python project into multiple source files.
- Use Git branches and commits to organize our work.
- Collaborate through GitHub and Pull Requests.
- Review and improve each other's code.

---

## How to Use This Repository

Clone the repository to your computer using Git:

```bash
git clone https://github.com/jeanne-le-roux-web/IEAP-python-series03.git
```

---
