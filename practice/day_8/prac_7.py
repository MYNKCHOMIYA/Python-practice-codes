def remove(lst):
 a =input("Enter the element to be removed: ").strip()
 
 if a in lst:
     lst.remove(a)
 else:
      print("Element not found in the list")
          

n = int(input("Enter the number of element: "))
lst = []
for  _ in range(n):
      element = input("Enter the element: ").strip()
      lst.append(element)
      print("The list is: ",lst)

remove(lst)
print("The list after removing the element is: ",lst)

