from people import *

from datetime import date

dob1 = date.fromisoformat('2000-08-01')
start_year1 = date.fromisoformat('2020-08-01')
hiring_year1 = date.fromisoformat('2021-08-01')


# Create a Student instance

john = Student("UT-ST-001", "John", "Doe", dob1, start_year1)

john.add_course("CS313")
john.add_course("CS329")

print(john)


# Create a professor instance
print("########################")

mike = Professor("UT-ST-002", "Mike", "Doe", dob1, start_year1, 6000, ["ML", "Data Stream"])

mike.add_courses(["CS313", "CS329", "CS378"])
print(mike)


# Create a staff member
print("########################")


# Create a Student instance

julia = Student("UT-ST-003", "chris", "Doe", dob1, start_year1)

julia.add_course("CS313")
julia.add_course("CS329")

print(julia)


# Create a Staff Member

matt = Staff("UT-ST-004", "Matt", "Doe", dob1, hiring_year1, 1000000)
print(matt)



# Create a Teaching Assistant

chris = Teaching_Assistant("UT-ST-005",    "Matt",   "Doe", dob1, start_year1, hiring_year1, 1000)
#
# chris.add_course("CS313")
# chris.add_course("CS329")

print(chris)


