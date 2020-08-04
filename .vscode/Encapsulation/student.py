# class Student:
#     def __init__(self):
#         self.__id = 123                         #Making the feilds private
#         self.__name = 'John'

#     def display(self):
#         print(self.__id)
#         print(self.__name)


# s = Student()
# # print(s.id)                                     #This will give error because id is private
# # print(s.__name)                                 #This will still give error as we cannot access it directly through the object

# s.display()                                        # Any private variables can only be accessed through methods of the class
# print(s._Student__id)                              # Name mangling syntax to access private fields(object._ClassName__VariableName)
# print(s._Student__name)
# s.display()


# Generally encapsulation is acheived through mutator methods - setId(),setName() where we are changing the names and
# accessor methods - getId(), getName() where we are obtaining the values
 
class Student:
    def setId(self,id):
        self.id = id

    def getId(self):
        return self.id
    
    def setName(self,name):
        self.name = name
    
    def getName(self):
        return self.name

s = Student()
s.setId(123)
s.setName('Mary')
print(s.getId())
print(s.getName())

    