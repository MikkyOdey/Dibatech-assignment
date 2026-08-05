# GRADE CLASS
class Grade:
    def __init__(self, sid, course, score):
        # store student details
        self.sid = sid
        self.course = course
        self.score = score

        # calculate grade immediately
        self.grade = self.get_grade()

    def get_grade(self):
        # convert score to grade
        if self.score >= 70: return "A"
        elif self.score >= 60: return "B"
        elif self.score >= 50: return "C"
        elif self.score >= 45: return "D"
        return "F"

    def show(self):
        # display student grade info
        print(f" My id is {self.sid} and my name is {self.course}, and I was a ble to score {self.score} which is a {self.grade}")


# Create an empty list to store grade
grades = []


# add grade
grades.append(
    Grade(
        input("Enter Student ID: "),
        input("Enter Course Name: "),
        int(input("Enter Score: "))
    )
)

print("\nGrade added successfully!")


# view grade
print("\nALL GRADES")
for g in grades:
    g.show()


# update grade
sid = input("\nEnter Student ID to Update: ")

for g in grades:
    if g.sid == sid:
        # update values
        g.course = input("New Course Name: ")
        g.score = int(input("New Score: "))

        # recalculate grade after update
        g.grade = g.get_grade()

        print("Grade Updated Successfully!")
        break
else:
    print("Student Not Found!")


# Average score
if grades:
    total = sum(g.score for g in grades)
    avg = total / len(grades)
    print("\nAverage Score:", avg)
else:
    print("\nNo Grades Available")


# delete grade
sid = input("\nEnter Student ID to Delete: ")

for g in grades:
    if g.sid == sid:
        grades.remove(g)
        print("Grade Deleted Successfully!")
        break
else:
    print("Student Not Found!")


