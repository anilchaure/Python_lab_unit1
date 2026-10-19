"""3) Write a program that accepts a student's marks in 5 subjects, computes the average, and
assigns a grade (A/B/C/D/F) using if-elif-else. Also check and display whether the student has
passed all subjects individually (each subject ≥ 35)."""

# Program 3: Student Grading System

m1 = int(input("Enter marks in subject 1: "))
m2 = int(input("Enter marks in subject 2: "))
m3 = int(input("Enter marks in subject 3: "))
m4 = int(input("Enter marks in subject 4: "))
m5 = int(input("Enter marks in subject 5: "))

total = m1 + m2 + m3 + m4 + m5
average = total / 5

print("Total Marks =", total)
print("Average Marks =", average)

if average >= 90:
    print("Grade A")
elif average >= 75:
    print("Grade B")
elif average >= 60:
    print("Grade C")
elif average >= 35:
    print("Grade D")
else:
    print("Grade F")

if m1 >= 35 and m2 >= 35 and m3 >= 35 and m4 >= 35 and m5 >= 35:
    print("Passed in all subjects")
else:
    print("Failed in one or more subjects")
