print("enter a string")
a = input();
if "  " in a:
      print("double space is present")
else:
      print("double space is not present");
replace = a.replace("  ", " ")
print("string after replacing double space with single space: \n", replace);