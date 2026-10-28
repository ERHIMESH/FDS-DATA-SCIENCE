# Topic: Practice question - rank student names using argsort | Source: Slide-3.pdf, page 29.

import numpy as np

# Reuse the names and marks shown in the argsort example on page 20.
names = np.array(["Aman", "Riya", "Kabir", "Neha"])
marks = np.array([78, 45, 92, 60])
order = np.argsort(marks)[::-1]
print(names[order])
print(marks[order])
