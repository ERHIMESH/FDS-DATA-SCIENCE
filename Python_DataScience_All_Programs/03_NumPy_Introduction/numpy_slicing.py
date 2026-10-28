# Topic: One-dimensional NumPy slicing | Source: Slide-2.pdf, page 12.

import numpy as np

marks = np.array([75, 82, 90, 68, 88])
print(marks[1:4])  # [82 90 68]
print(marks[:3])  # [75 82 90]
print(marks[2:])  # [90 68 88]
print(marks[::2])  # [75 90 88]

# The stop index is excluded; basic slicing usually returns a view.
