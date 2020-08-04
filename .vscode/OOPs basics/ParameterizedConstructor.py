# Create a class Course with following information - name, rating

class Course:
    def __init__(self,name,rating):                 #define all th parametrs that we want to pass in
        self.name = name
        self.rating = rating

# Define a method to calculate the average ratings of the course

    def average(self):
        numberOfRating = len(self.rating)
        average = sum(self.rating)/numberOfRating
        print('Average rating for', self.name, 'is', average)

c1 = Course('Java course',[1,2,3,4,5])
print(c1.name)
print(c1.rating)
c1.average()                                 #Invoking the method

c2 = Course('Java web services',[5,5,5,5,5])
print(c2.name)
print(c2.rating)
c2.average()


