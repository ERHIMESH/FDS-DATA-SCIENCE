# Topic: Sorting 1D arrays in ascending and descending order | Source: Slide-3.pdf, page 18.

import numpy as np

marks = np.array([78, 45, 92, 60, 85])
print(np.sort(marks))
print(np.sort(marks)[::-1])
print("Original:", marks)

# Outputs:
# [45 60 78 85 92]
# [92 85 78 60 45]
# Original: [78 45 92 60 85]
