marks = []
student_number = 1
mark_input = float(input("Enter mark for first student: "))

while mark_input >= 0:
    student_number += 1
    marks += [mark_input]
    print("Enter mark for student number", student_number)
    mark_input = float(input("Enter mark: "))

print(marks)


def get_higher_note():
    higher_note = float(0)
    for i in range(len(marks)):
        note = marks[i]
        if note >= higher_note:
            higher_note = note
    return higher_note


def get_lowest_note():
    lower_note = float(10)
    for i in range(len(marks)):
        note = marks[i]
        if note < lower_note:
            lower_note = note
    return lower_note


def get_average_note():
    sum_of_all_marks = sum(marks)
    average = sum_of_all_marks / (len(marks))
    return average


def attendance():
    attendance = len(marks)
    return attendance


print("The higher mark is:", get_higher_note())
print("The lowest mark is:", get_lowest_note())
print("The average mark is:", get_average_note())
print("The attendance is:", attendance())
