# Topic: Random matrices, decimals, and normal samples | Source: Slide-3.pdf, page 22.

import numpy as np

rng = np.random.default_rng(42)
marks = rng.integers(35, 101, size=(4, 3))
print(marks.shape)  # (4, 3)

values = rng.random(5)  # 0 <= value < 1
scores = rng.normal(loc=70, scale=10, size=5)
print(values)
print(scores)
