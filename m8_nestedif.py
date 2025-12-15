#nested if else

marks = float(input("Enter your marks "))
if marks >= 60 :
    print("Congratulations you have passed the Exam and scored above 60")
    if marks >= 90:
        print("Your marks is greater than 90, grade is A")
    elif marks >= 80 and marks <= 89:
        print("Your marks is greater than 80, grade is B")
    elif marks >= 70 and marks <= 79:
        print("Your marks is greater than 70, grade is C")
    elif marks >= 60 and marks <= 69:
        print("Your marks is greater than 60, grade is D")
else:
    print("you have failed the Exam and scored below 60")

'''
#if-elif-else

>= 90 , grade A
80 and 89 grade b
70 and 79 grade c
60 and 69 grade d
<60 , grade F
'''
'''
marks = float(input("Enter your marks "))
if marks >= 90:
    print("Your marks is greater than 90, grade is A")
elif marks >= 80 and marks <= 89 :
    print("Your marks is greater than 80, grade is B")
elif marks >= 70 and marks <= 79 :
    print("Your marks is greater than 70, grade is C")
elif marks >= 60 and marks <= 69 :
    print("Your marks is greater than 60, grade is D")
else :
    print("Your are failed, grade is F")
 '''