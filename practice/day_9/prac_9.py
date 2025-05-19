# i works it on  previous (prac_9.py) practice que
with open("this.txt","r") as this:
   g = this.read()
   print(" give a file for save the copy paste : ")
   file_name=input()

with open(file_name,"w") as copy:
     copy.write(g) 
    
with open(file_name,"r") as check:
    copied_content= check.read()
 
if copied_content == g :
   print("thats is a copy paste")
else:
   print("thats didnt works")