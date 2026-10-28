# Topic: Inspecting and setting NumPy data types | Source: Slide-2.pdf, page 9.

import numpy as np

a = np.array([10, 20, 30])
b = np.array([1.5, 2.5, 3.5])
c = np.array([True, False, True])

print(a.dtype)
print(b.dtype)
print(c.dtype)

marks = np.array([75, 80, 90], dtype=np.float32)
print(marks.dtype)  # float32
