# Topic: Comparing a loop and a vectorized expression | Source: Slide-2.pdf, page 16.

import numpy as np

marks = np.array([60, 70, 80, 90])

updated = []
for mark in marks:
    updated.append(mark + 5)

updated_numpy = marks + 5
print("Loop:", updated)
print("NumPy:", updated_numpy)

# Both approaches produce [65, 75, 85, 95].
