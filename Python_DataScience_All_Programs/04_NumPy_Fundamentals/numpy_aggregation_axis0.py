# Topic: Column-wise aggregation with axis=0 | Source: Slide-3.pdf, page 12.

import numpy as np

# Rows are students; columns are subjects, as in the matrix on page 11.
marks = np.array([[70, 80, 90], [60, 75, 85], [90, 95, 80]])
print("Sum:", np.sum(marks, axis=0))
print("Mean:", np.mean(marks, axis=0))

# Output:
# Sum:  [220 250 255]
# Mean: [73.33 83.33 85.00] (as displayed on the slide)
