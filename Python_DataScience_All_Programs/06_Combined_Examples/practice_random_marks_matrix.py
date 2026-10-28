# Topic: Practice question - generate a reproducible 4x5 marks matrix | Source: Slide-3.pdf, page 29.

import numpy as np

rng = np.random.default_rng(42)
marks = rng.integers(40, 101, size=(4, 5))
print(marks)
