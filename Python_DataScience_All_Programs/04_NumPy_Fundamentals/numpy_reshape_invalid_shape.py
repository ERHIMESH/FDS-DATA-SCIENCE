# Topic: Demonstrating an invalid reshape | Source: Slide-3.pdf, page 17.

import numpy as np

numbers = np.arange(1, 13)

# Original slide expression; it raises ValueError because 5 * 3 != 12.
# print(numbers.reshape(5, 3))

# Catch the expected error so the demonstration remains runnable to completion.
try:
    print(numbers.reshape(5, 3))
except ValueError as error:
    print(f"Expected ValueError: {error}")
