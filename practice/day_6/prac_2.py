s1= int(input("enter the number of students in first subject: "))
s2= int(input("enter the number of students in second subject: "))
s3= int(input("enter the number of students in third subject: "))
total_marks=300
sm = s1 + s2 + s3
percentage = (sm/total_marks)*100
if s1>33 and s2>33 and s3>33 and percentage>40:
    print("the student is pass")
else :
      print("the student is fail")