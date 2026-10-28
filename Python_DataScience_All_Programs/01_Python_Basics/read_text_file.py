# Topic: Reading a text file | Source: Slide-1.pdf, page 12.

from pathlib import Path

students_file = Path(__file__).with_name("students.txt")
with students_file.open("r", encoding="utf-8") as file:
    content = file.read()

print(content)

# Common modes: "r" = read, "w" = write/overwrite, "a" = append.
