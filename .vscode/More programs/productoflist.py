#Input a list from the user and calculate the product of all the numbers
lst=[int(lst) for lst in input('Enter the numbers separated by space: ').split(' ')]
#print(len(lst))

pdt=1
for i in lst:
    pdt=pdt*i
    i=i+1
print(pdt)
