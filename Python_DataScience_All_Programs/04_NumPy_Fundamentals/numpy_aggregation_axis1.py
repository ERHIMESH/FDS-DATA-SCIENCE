# Topic: Row-wise aggregation with axis=1 | Source: Slide-3.pdf, page 13.

import numpy as np

marks = np.array([[70, 80, 90], [60, 75, 85], [90, 95, 80]])
print("Sum:", np.sum(marks, axis=1))
print("Mean:", np.mean(marks, axis=1))

# Output:
# Sum:  [240 220 265]
# Mean: [80.00 73.33 88.33] (as displayed on the slide)
