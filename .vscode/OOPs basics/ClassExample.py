class Employee:                                         

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@company.com'

    def fullname(self):
        return print(self.first + ' ' + self.last)


emp1 = Employee('Corey','Schafer',50000)
emp2 = Employee('Ted','Mosbey',60000)


emp1.fullname()
print(Employee.fullname(emp1))
emp2.fullname()


    

