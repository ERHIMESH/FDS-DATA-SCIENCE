# Topic: Common NumPy array creation functions | Source: Slide-2.pdf, page 6.

import numpy as np

zeros = np.zeros(5)
ones = np.ones(4)
sequence = np.arange(1, 6)
evenly_spaced = np.linspace(0, 10, 5)
from_values = np.array([2, 4, 6])

print("zeros:", zeros)
print("ones:", ones)
print("arange:", sequence)
print("linspace:", evenly_spaced)
print("array:", from_values)

# Typical outputs:
# zeros: [0. 0. 0. 0. 0.]
# ones: [1. 1. 1. 1.]
# arange: [1 2 3 4 5]
# linspace: [ 0.   2.5  5.   7.5 10. ]
