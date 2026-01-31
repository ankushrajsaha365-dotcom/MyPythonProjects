# Task

# Constructor takes:
# name
# marks in 3 subjects

# Method:
# calculates total
# prints Pass / Fail (pass if total ≥ 120)



class Exam:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def evaluate(self):
        if len(self.marks) != 3:
            print("Error: Enter marks for exactly 3 subjects")
            return

        total = sum(self.marks)

        if total >= 120:
            print(f"{self.name} has passed the exam")
        else:
            print(f"{self.name} has failed the exam")


name = input("Enter student's name: ")
marks = list(map(int, input("Enter marks in 3 subjects: ").split()))

exam = Exam(name, marks)
exam.evaluate()
