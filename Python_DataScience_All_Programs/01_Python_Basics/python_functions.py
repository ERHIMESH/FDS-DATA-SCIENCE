# Topic: Python functions and averages | Source: Slide-1.pdf, page 10.


def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average


marks = [80, 70, 90, 60, 85]
result = calculate_average(marks)

print("Average marks:", result)
