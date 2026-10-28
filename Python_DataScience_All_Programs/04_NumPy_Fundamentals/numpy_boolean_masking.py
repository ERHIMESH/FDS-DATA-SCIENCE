# Topic: Selecting 1D values with a Boolean mask | Source: Slide-3.pdf, page 6.

import numpy as np

marks = np.array([45, 78, 92, 60, 85])
mask = marks >= 75
print(mask)
print(marks[mask])

# Output:
# [False  True  True False  True]
# [78 92 85]
