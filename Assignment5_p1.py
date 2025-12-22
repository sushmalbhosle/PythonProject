
# creating dict of student marks

student_marks = {
    'John': 85,'sam': 65,'hash': 98,'Sandy': 80,'Bob': 90,
}

student_name = input('Enter your name to see marks: ')

marks = student_marks.get(student_name)

if marks is not None:
    print(f"student name is {student_name} and your marks is {marks}")
else:
    print("student name is not present in the record ")