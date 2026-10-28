# Topic: Inspecting the number of array dimensions | Source: Slide-2.pdf, page 7.

import numpy as np

a = np.array([10, 20, 30])
b = np.array([[10, 20, 30], [40, 50, 60]])
c = np.array([[[1, 2], [3, 4]]])

print(a.ndim)  # 1
print(b.ndim)  # 2
print(c.ndim)  # 3
