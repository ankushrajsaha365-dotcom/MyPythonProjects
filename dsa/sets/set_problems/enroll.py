# Students Enrolled in Courses

# Two sets represent students enrolled in two courses.
# Find:

# 1-> Students in both courses

# 2-> Students in only one course

# 3-> Total unique students



course1 = set(map(int,input("Enter student id:").split()))
course2 = set(map(int,input("Enter student id:").split()))

# 1. Students in both courses
print("Students in both courses:", course1 & course2)

# 2. Students in only one course
print("Students in only one course:", course1 ^ course2)

# 3. Total unique students
print("Total unique students:", course1 | course2)
