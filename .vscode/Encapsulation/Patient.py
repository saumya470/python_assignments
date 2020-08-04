class Patient:

    def setId(self,id):
        self.id = id

    def getId(self):
        return self.id

    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name

    def setSsn(self,ssn):
        self.ssn = ssn

    def getSsn(self):
        return self.ssn

p = Patient()
p.setId(11243)
p.setName('Lucy Danes')
p.setSsn('231-110-7432')
print(p.getId())
print(p.getName())
print(p.getSsn())
