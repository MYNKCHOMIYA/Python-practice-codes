def pattern(n):
      for i in range(0,n):
                                  print("*"*(n-i),end="\n")            

n = int(input("Enter the number of rows: "))
pattern(n)
print()            