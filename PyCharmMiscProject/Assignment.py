
# Assignment Class
class Assignment:
    def __init__(self, title, course, due_date, description):
        self.title = title
        self.course = course
        self.due_date = due_date
        self.description = description

    def display(self):
        print("\nTitle:", self.title)
        print("Course:", self.course)
        print("Due Date:", self.due_date)
        print("Description:", self.description)


# Empty list to store assignments
assignments = []


# CREATE ASSIGNMENT
title = input("Enter Assignment Title: ")
course = input("Enter Course Name: ")
due_date = input("Enter Due Date: ")
description = input("Enter Description: ")

assignment = Assignment(title, course, due_date, description)
assignments.append(assignment)

print("\nAssignment Added Successfully!")


# VIEW ASSIGNMENTS
print("\nAll Assignments")
for assignment in assignments:
    assignment.display()

# EDIT ASSIGNMENT
search_title = input("Enter Assignment Title to Edit: ")

for assignment in assignments:
    if assignment.title == search_title:
        print("\nCurrent Assignment Details")
        assignment.display()

        assignment.title = input("New Title: ")
        assignment.course = input("New Course Name: ")

        print("\nAssignment Updated Successfully!")

        # Display updated assignment immediately
        assignment.display()
        break
else:
    print("Assignment Not Found!")

# Delete assignment
delete_title = input("Enter Assignment Title to Delete: ")

for assignment in assignments:
    if assignment.title == delete_title:
        assignments.remove(assignment)
        print("Assignment Deleted Successfully!")
        break
else:
    print("Assignment Not Found!")