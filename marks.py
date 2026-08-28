r=int(input("Enter the total marks of subject:"))
a=int(input("Enter the marks of maths:"))
b=int(input("Enter the marks of physics:"))
c=int(input("Enter the marks of chemistry:"))
d=int(input("Enter the marks of english:"))
e=int(input("Enter the marks of biology:"))
avg=((a+b+c+d+e)/5)
percentage=((avg/r)*100)
print("The total percentage is",((avg/r)*100))
if(percentage<=40):
   print("Fail")
elif(percentage<40):  
   print("II class")
elif(percentage<=65):
   print("I class")   
elif(percentage<=75):
   print("Distinction")
else:
   print("Outstanding")
