Marks = int(input("Enter marks: "))

if Marks >= 90:
    grade = "O"
elif Marks >= 80:
    grade = "A"
elif Marks >= 70:
    grade = "B"
elif Marks >= 60:
    grade = "C"
elif Marks >= 50:
    grade = "D"
elif Marks >= 40:
    grade = "E"
else:
    grade = "F"

print(f"Grade: {grade}")