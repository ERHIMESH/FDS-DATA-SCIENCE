# Topic: Student records, functions, loops, and pass status | Source: Slide-1.pdf, page 15.

students = [
    {"name": "Aman", "marks": [78, 85, 72]},
    {"name": "Riya", "marks": [92, 88, 95]},
    {"name": "Mohit", "marks": [35, 48, 55]},
    {"name": "Neha", "marks": [65, 74, 80]},
]


def average(marks):
    return sum(marks) / len(marks)


for student in students:
    avg = average(student["marks"])
    status = "Pass" if avg >= 40 else "Needs support"
    print(student["name"], round(avg, 2), status)

# The source checks the average only; subject-wise pass rules may differ.
