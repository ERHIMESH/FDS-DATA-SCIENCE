# Topic: Student marks analysis with basic NumPy operations | Source: Slide-2.pdf, page 17.

import numpy as np

# Three students and four subjects.
marks = np.array(
    [
        [75, 80, 90, 85],
        [65, 70, 85, 75],
        [88, 92, 78, 95],
    ]
)

print("Marks matrix:\n", marks)
print("Dimensions:", marks.ndim)
print("Shape:", marks.shape)
print("Data type:", marks.dtype)
print("First mark:", marks[0, 0])
print("First two students:\n", marks[:2, :])

updated_marks = marks + 5
print("Updated marks:\n", updated_marks)
print("Marks >= 80:\n", marks[marks >= 80])
