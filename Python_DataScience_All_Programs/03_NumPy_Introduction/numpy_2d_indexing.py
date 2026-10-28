# Topic: Two-dimensional row and column indexing | Source: Slide-2.pdf, page 11.

import numpy as np

marks = np.array([[75, 80, 90], [65, 70, 85]])
print(marks[0, 0])  # 75
print(marks[0, 2])  # 90
print(marks[1, 1])  # 70
print(marks[1, 2])  # 85, second row and third column
