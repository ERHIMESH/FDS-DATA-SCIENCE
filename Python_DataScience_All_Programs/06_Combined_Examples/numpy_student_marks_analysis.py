# Topic: Integrated random marks analysis | Source: Slide-3.pdf, page 26.

import numpy as np

rng = np.random.default_rng(42)
marks = rng.integers(40, 101, size=(5, 4))
print("Original marks:\n", marks)

# Add subject-wise bonus using broadcasting.
bonus = np.array([2, 3, 1, 4])
updated = marks + bonus
print("Updated marks:\n", updated)

# One average per student.
averages = np.mean(updated, axis=1)
print("Student averages:", averages)

# Filter qualifying averages.
print("Averages >= 75:", averages[averages >= 75])

# One average per subject.
print("Subject averages:", np.mean(updated, axis=0))

# Rank averages in descending order.
order = np.argsort(averages)[::-1]
print("Ranked averages:", averages[order])
