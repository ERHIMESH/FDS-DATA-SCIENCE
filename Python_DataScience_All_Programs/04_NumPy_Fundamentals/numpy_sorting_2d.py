# Topic: Sorting a 2D array along rows and columns | Source: Slide-3.pdf, page 19.

import numpy as np

marks = np.array([[70, 90, 60], [85, 65, 95]])
print("axis=1:", np.sort(marks, axis=1))
print("axis=0:", np.sort(marks, axis=0))

# axis=1 sorts each row; axis=0 sorts down each column.
