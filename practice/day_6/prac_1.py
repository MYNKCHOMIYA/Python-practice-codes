a= int(input("enter the first number: "))
b=int(input("enter the second number: "))
c=int(input("enter the third number: "))
d=int(input("enter the fourth number: "))
if(a<b and c<d and b<d):
      print("d is greatest");
elif(b<a and c<a and d<a):
      print("a is greatest"); 
elif(a<c and b<c and d<c):
      print("c is greatest");
else:
      print("b is greatest"); 

