student_scores = {"Alice": 85, "Bob": 90}
name = input("Enter student name: ")
score = student_scores.get(name)
if score is not None:
    print(score)
else:
    print("Not Found")
