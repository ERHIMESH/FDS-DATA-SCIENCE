# Topic: Boolean filtering of values in a 2D array | Source: Slide-3.pdf, page 8.

import numpy as np

marks = np.array([[45, 80, 70], [90, 85, 95], [30, 50, 40]])
print(marks[marks >= 80])

# Output: [80 90 85 95]
# A scalar condition selects qualifying values as a 1D array.
