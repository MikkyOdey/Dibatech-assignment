# creating a variable and assigning values
USERNAME = "mike"
PASSWORD = "uber"

# to ask username and password
username = input("Enter username: ")
password = input("Enter password: ")

if username == USERNAME and password == PASSWORD:
    print("Login Successful")
else:
    print("Login Failed")

# creating  an empty list that will hold all the student's record
students = []

# ask user to enter student's details using input function
student_id = input("enter student ID: ")
name = input("Enter Full Name: ")
email = input("Enter email: ")
phone = input("Enter phone number: ")
programme = input("Enter programme: ")
date = input("Enter Registration date: ")

# store them in a dictionary
student = {
    "id": student_id,
    "name": name,
    "email": email,
    "phone": phone,
    "programme": programme,
    "date": date
}
# add the dictionary to the list
students.append(student)

#use 'for loop' to list all the student's details
for student in students:
    print(student)

# to update student's information, search for student id using input function
search_id = input("Enter student id: ")

# using for loop and conditional statement to check student's details on the list
for student in students:
    if student["id"] == search_id:
        print(student)

# update the name by replacing it with a new one
student["name"] = input("New Name: ")
search_id = input("Enter student id: ")
for student in students:
    if student["id"] == search_id:
        print(student)

students = [
    {"id": "11"},
    {"id": "22"}
]

student_id = input("Enter Student ID to delete: ")

for student in students:
    if student["id"] == student_id:
        students.remove(student)
        print("Student deleted successfully!")
        break
else:
    print("Student not found!")

print(students)






