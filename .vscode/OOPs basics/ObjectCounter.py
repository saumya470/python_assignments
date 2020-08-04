class ObjectCounter:

    NumOfObjects = 0

    def __init__(self):
        ObjectCounter.NumOfObjects+=1

    @staticmethod
    def displayCount():
        print(ObjectCounter.NumOfObjects)

o1 = ObjectCounter()
o2 = ObjectCounter()

ObjectCounter.displayCount()




