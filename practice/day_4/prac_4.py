n = int(input("enter the number of int numnbers: "))
numbers=[];
for i in range(n):
      element = int(input("enter the number: "))
      numbers.append(element);
print("list of numbers: ", numbers);
print("sum of numbers: ", sum(numbers));