# Topic: Ranking student names with argsort | Source: Slide-3.pdf, page 20.

import numpy as np

names = np.array(["Aman", "Riya", "Kabir", "Neha"])
marks = np.array([78, 45, 92, 60])
order = np.argsort(marks)[::-1]
print(names[order])
print(marks[order])

# Output:
# ['Kabir' 'Aman' 'Neha' 'Riya']
# [92 78 60 45]
