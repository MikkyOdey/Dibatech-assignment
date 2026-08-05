# Create class
class Announcement:
    def __init__(self, title, date, message):
        # store announcement details
        self.title = title
        self.date = date
        self.message = message

    def show(self):
        # display announcement
        print("\nTitle:", self.title)
        print("Date:", self.date)
        print("Message:", self.message)


# Create an empty list to store data
announcements = []


# Create announcement
announcements.append(
    Announcement(
        input("Enter Title: "),
        input("Enter Date: "),
        input("Enter Message: ")
    )
)

print("\nAnnouncement Created Successfully!")


# view announcement
print("\nALL ANNOUNCEMENTS")
for a in announcements:
    a.show()

# to delete
title = input("\nEnter Title to Delete: ")

for a in announcements:
    if a.title == title:
        announcements.remove(a)
        print("Announcement Deleted Successfully!")
        break
else:
    print("Announcement Not Found!")
