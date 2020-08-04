m,c,p=int(input('Enter the marks in maths:')),int(input('Enter marks in physics:')),int(input('Enter marks in chem:'))
if(m<35 or p<35 or c<35): print('You have failed in one or more subjects')
elif((m+c+p)/3<=59): print('Congralutions your average is:',round((m+c+p)/3,2),'Your grade is C')
elif((m+c+p)/3<=69): print('Congralutions your average is:',round((m+c+p)/3,2),'Your grade is B')
else: print('Congralutions your average is:',round((m+c+p)/3,2),'Your grade is A')  



    