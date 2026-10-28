# Topic: Inspecting array shape | Source: Slide-2.pdf, page 8.

import numpy as np

marks = np.array([[75, 80, 90], [65, 70, 85]])
print(marks.shape)  # (2, 3)

a = np.array([10, 20, 30, 40])
print(a.shape)  # (4,)
