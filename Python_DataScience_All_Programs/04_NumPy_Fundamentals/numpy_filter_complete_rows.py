# Topic: Filtering complete rows with a Boolean mask | Source: Slide-3.pdf, page 9.

import numpy as np

marks = np.array([[45, 80, 70], [90, 85, 95], [30, 50, 40]])

print(marks[:, 0])
print(marks[:, 0] >= 40)
print(marks[marks[:, 0] >= 40])

# Output:
# [45 90 30]
# [ True  True False]
# [[45 80 70]
#  [90 85 95]]
