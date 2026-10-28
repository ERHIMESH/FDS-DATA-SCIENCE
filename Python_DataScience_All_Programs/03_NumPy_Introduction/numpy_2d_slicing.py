# Topic: Selecting a rectangular portion of a 2D array | Source: Slide-2.pdf, page 13.

import numpy as np

marks = np.array([[75, 80, 90], [65, 70, 85], [88, 92, 78]])
print(marks[0:2, 0:2])

# Output:
# [[75 80]
#  [65 70]]
