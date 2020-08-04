# class Student:
#     name='Rohan'
#     age=16

# s1=Student()
# s2=Student()
# print(s1.name,end='')
# print(s2.name,end='')


# class change:
#     def __init__(self,x,y,z):
#         self.a=x+y+z

# x=change(1,2,3)
# y=getattr(x,'a')
# setattr(x,'a',y+1)

class A:
    def __init__(self):
        self.x=1
        self.__y=1
    def getY(self):
        return self.__y
a=A()
a.__y=45
print(a.getY())
