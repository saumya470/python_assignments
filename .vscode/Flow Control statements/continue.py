#Print all numbers between 1 to 50 and skip multiples of 3
num=1
for num in range(1,51):
    if(num%3==0):
        continue #This will continue typing the remaining numbers (after just skipping multoiples of 3)
    print(num)
    num+=num
 
 # Break will just stop the loop at the first occurrence of 3

