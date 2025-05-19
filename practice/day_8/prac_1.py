def greatest(a,b,c):
      if a>b and a>c:
            return "a is greatest"
      elif b>a and b>c:
            return "b is greatest"
      elif c>a and c>b:
            return "c is greatest"
      else:
            return "all are equal"
a = int(input("Enter a: "))
b = int(input("Enter b: "))   
c = int(input("Enter c: "))
print(greatest(a,b,c))