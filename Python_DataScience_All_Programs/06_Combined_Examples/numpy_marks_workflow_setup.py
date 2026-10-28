# Topic: Generating marks and applying subject bonuses | Source: Slide-3.pdf, page 25.

import numpy as np

rng = np.random.default_rng(42)
marks = rng.integers(40, 101, size=(5, 4))
bonus = np.array([2, 3, 1, 4])
updated_marks = marks + bonus

print("Original marks:\n", marks)
print("Updated marks:\n", updated_marks)
