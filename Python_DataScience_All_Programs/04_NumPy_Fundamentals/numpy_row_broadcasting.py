# Topic: Broadcasting one subject bonus across matrix rows | Source: Slide-3.pdf, page 4.

import numpy as np

marks = np.array([[60, 70, 80], [75, 85, 90]])
bonus = np.array([5, 10, 15])
result = marks + bonus
print(result)

# Output:
# [[ 65  80  95]
#  [ 80  95 105]]
