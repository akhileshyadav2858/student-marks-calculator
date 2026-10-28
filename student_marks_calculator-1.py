# Student Marks Calculator
# Beginner Python project by Akhilesh Yadav

student_name = input("Enter student name: ")

subjects = ["English", "Mathematics", "Physics", "Chemistry", "Computer"]
marks = []

for subject in subjects:
    while True:
        try:
            score = float(input(f"Enter marks in {subject} (0-100): "))
            if 0 <= score <= 100:
                marks.append(score)
                break
            print("Please enter marks between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

total = sum(marks)
percentage = total / len(subjects)
passed = all(score >= 33 for score in marks)

print("\n" + "=" * 32)
print("       STUDENT RESULT")
print("=" * 32)
print(f"Name       : {student_name}")
print(f"Total      : {total:g} / {len(subjects) * 100}")
print(f"Percentage : {percentage:.2f}%")
print(f"Result     : {'PASS' if passed else 'FAIL'}")
print("=" * 32)
