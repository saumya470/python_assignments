from collections import Counter

lst1 = input('Enter string elements separated by space:').split(' ')
ch=input('Enter the character to find:')


distint_list=list(Counter(lst1).keys())
lst2=[]

for i in range(len(distint_list)):
    elmnt=distint_list[i]
    if elmnt.count(ch)>0:
        for j in range(elmnt.count(ch)):
            lst2.insert(i,elmnt)

print(lst2)
