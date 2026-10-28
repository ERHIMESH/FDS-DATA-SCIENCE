# Topic: Comparing indexing and slicing | Source: Slide-2.pdf, page 14.

import numpy as np

marks = np.array([75, 82, 90, 68, 88])
print(marks[2])  # 90: indexing returns one value
print(marks[1:4])  # [82 90 68]: slicing returns an array
