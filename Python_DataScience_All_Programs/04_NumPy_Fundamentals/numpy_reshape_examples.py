# Topic: 2D, 3D, and inferred-dimension reshaping | Source: Slide-3.pdf, page 16.

import numpy as np

numbers = np.arange(1, 13)
print(numbers.reshape(3, 4))
print(numbers.reshape(1, 3, 4).shape)
print(numbers.reshape(3, -1))

# Example output shape: (1, 3, 4)
