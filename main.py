from teacherClass import Teacher
from studentClass import Student, marks_upload

"""
    This Student Attendance Management can input entries to the JSON files either by directly using objects or by manually providing entries.
"""

# First: Entries through Object Initialization 
"""
The contents of the initialized objects must be changed, in case of providing new entries. This can be done for both students.json and teachers.json file.
"""

# For Teacher Class
t1 = Teacher('sachin', 'maths', '123', 'sachin@gmail.com', '3456789088', 'sachin nagar')
t2 = Teacher('jim', 'programming', '555', 'quinjet@gmail.com', '8392839282', 'jim beglin')
t3 = Teacher('John Doe', 'Math', '12345', 'john.doe@example.com', '1234567890', '123 Main St')
t4 = Teacher('John Zip', 'Social', '67788', 'zip.doe@example.com', '1278534890', '55 Main St')

print(t1.accept()) # Accepts provided entries
print(t2.accept())
print(t3.accept())
print(t4.accept())

# For Student Class
print('Provide marks for s1 object:\n')
marks = marks_upload()
s1 = Student('ramesh', '33', 'ramesh@gmail.com', '8392838328', marks, '333 Sub St')
print('Provide marks for s2 object:\n')
marks = marks_upload()
s2 = Student('manav', '39', 'zaza@gmail.com', '7382918292', marks, '999 Main Lane')

print(s1.accept()) # Accepts provided entries
print(s2.accept())


t1.display_all() # Displays all contents of the teachers.json file

print('Enter student name to search: ')
t1.search() # Search required entry in the teachers.json file 

"""
Providing entries through class methods, this allows for new entries in both teachers.json and student.json files.
"""

s1.authentication()

"""
Additional functionality: 
"""
s1.display_all() # Display all contents of the students.json file 
print('Enter name of student to search: ')
s1.search() # Same functionality as search() from Teacher Class but show grades, pass-fail info etc of requested student
s1.rank() # Ranks the requested students based on marks gained