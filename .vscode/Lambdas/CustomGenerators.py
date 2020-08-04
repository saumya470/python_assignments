# Generators are functions that return a sequence of values back using an yeild statement
# 
def customgen(x,y):
    while x<y:
        yield x
        x=x+1

result=customgen(20,30)

for i in result:print(i)