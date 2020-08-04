class Student:
    major = 'CSE'           #static variables which is common for all the objects of the class

    def __init__(self,rollno,name):               #rollno,name are instance variables
        self.rollno = rollno
        self.name = name

s1 = Student(1,'Mary')
s2 = Student(2,'Bill')


print(s1.major)
print(s2.major)
print(s1.name)
print(s2.name)
print(Student.major)            # A static variable can also be accessed directly  by the class name instaed of object name
