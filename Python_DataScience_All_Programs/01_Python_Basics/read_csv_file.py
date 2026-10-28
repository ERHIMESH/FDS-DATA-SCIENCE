# Topic: Reading rows from a CSV file | Source: Slide-1.pdf, page 13.

import csv
from pathlib import Path

students_file = Path(__file__).with_name("students.csv")
with students_file.open("r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

# CSV values are strings; convert them to numbers before calculations.
