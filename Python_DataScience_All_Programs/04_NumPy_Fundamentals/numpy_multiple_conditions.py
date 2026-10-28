# Topic: Boolean masking with multiple conditions | Source: Slide-3.pdf, page 7.

import numpy as np

marks = np.array([25, 45, 60, 75, 90])
mask = (marks >= 40) & (marks < 75)
print(marks[mask])

# Output: [45 60]
# NumPy array conditions use element-wise &, |, and ~ operators.
