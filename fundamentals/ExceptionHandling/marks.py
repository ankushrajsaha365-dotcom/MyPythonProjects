# marks of an exam
class MarksError(Exception):
    pass

try:
    a = int(input("Enter marks of sub A: "))
    b = int(input("Enter marks of sub B: "))
    c = int(input("Enter marks of sub C: "))

    marks_list = [a, b, c]

    for m in marks_list:
        if m not in range(0, 101):
            raise MarksError("Marks must be between 0 and 100")

except ValueError:
    print("Please enter valid integer marks")

except MarksError as e:
    print(e)

else:
    average = sum(marks_list) / len(marks_list)
    print("Average marks:", average)
