# Topic: Random choice, shuffle, and permutation | Source: Slide-3.pdf, page 23.

import numpy as np

# The source uses rng from the previous random-generation examples.
# Initialize it here so this file can run independently.
rng = np.random.default_rng(42)
students = np.array(["Aman", "Riya", "Kabir", "Neha", "Priya"])
selected = rng.choice(students, size=3, replace=False)

marks = np.array([60, 70, 80, 90, 95])
rng.shuffle(marks)  # Changes the array in place.
permuted = rng.permutation(students)

print("Selected:", selected)
print("Shuffled marks:", marks)
print("Permuted students:", permuted)
