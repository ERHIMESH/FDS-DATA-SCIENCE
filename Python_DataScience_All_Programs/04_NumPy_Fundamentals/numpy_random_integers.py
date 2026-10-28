# Topic: Reproducible random integer generation | Source: Slide-3.pdf, page 21.

import numpy as np

rng = np.random.default_rng(42)
marks = rng.integers(0, 101, size=5)
print(marks)

# Output: [ 8 77 65 43 43]
