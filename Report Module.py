students = []
assignments = []
grades = []
announcements = []
def generate_report():
    print(" \n ====REPORTS===")

    # Total students
    print("Total Students:", len(students))

    # Total assignments
    print("Total Assignments:", len(assignments))

    # Average score
    if grades:
        total = 0
        for g in grades:
            total += g["score"]

        print("Average Student Score:", total / len(grades))
    else:
        print("Average Student Score: No grades available")

    # Top student
    if grades:
        top = grades[0]

        for g in grades:
            if g["score"] > top["score"]:
                top = g

        print("\nTop-Performing Student:")
        print("Student ID:", top["student_id"])
        print("Score:", top["score"])
    else:
        print("\nTop-Performing Student: No grades available")

    # Recent students
    if students:
        print("\nRecently Registered Students:")
        for s in students[-3:]:
            print(s["id"], "-", s["name"])
    else:
        print("No students registered")
students = [
    {"id": "S001", "name": "John"},
    {"id": "S002", "name": "Mary"},
    {"id": "S003", "name": "Peter"},
    {"id": "S004", "name": "Alice"},
    {"id": "S005", "name": "Mark"}
]

assignments = [
    {"title": "Mathematics"},
    {"title": "English Language"},
    {"title": "Science Subject"}
]

grades = [
    {"student_id": "S002", "score": 80},
    {"student_id": "S003", "score": 95},
    {"student_id": "S001", "score": 69}
]

announcements = [
    {"title": "Exam Notice", "date": "2026-06-26", "message": "Exams will start next week."},
    {"title": "Holiday Update", "date": "2026-06-25", "message": "School will be closed on Friday."}
]

generate_report()