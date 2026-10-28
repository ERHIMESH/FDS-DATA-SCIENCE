# Topic: Filtering values with a Boolean mask | Source: Slide-2.pdf, page 16.

import numpy as np

marks = np.array([35, 45, 80, 28, 60])
print(marks[marks >= 40])

# Output: [45 80 60]
