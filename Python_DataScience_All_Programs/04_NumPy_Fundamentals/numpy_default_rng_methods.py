# Topic: Common default_rng methods | Source: Slide-3.pdf, page 24.

import numpy as np

rng = np.random.default_rng(42)
students = np.array(["Aman", "Riya", "Kabir", "Neha", "Priya"])
data = students.copy()

print("integers:", rng.integers(1, 10, size=5))
print("random:", rng.random(5))
print("normal:", rng.normal(70, 10, size=5))
print("choice:", rng.choice(data, size=3))

rng.shuffle(data)
print("shuffle:", data)
print("permutation:", rng.permutation(data))

# The slide's choice(data, ...) examples use a generic data variable;
# this uses the student names shown on page 23.
