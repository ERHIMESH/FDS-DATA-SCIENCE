# Topic: Practice question - select marks at least 70 | Source: Slide-3.pdf, page 29.

import numpy as np

# The question does not supply an input array; reuse marks from page 18.
marks = np.array([78, 45, 92, 60, 85])
print(marks[marks >= 70])
