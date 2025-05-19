a = {"dost":"friend",
     "kutta":"dog",
     "panni":"water",
     "garmi":"summer",}
print("give a word within the ",list(a.keys()), "to get the meaning: ");
input_word = input();
if input_word in a:
    print("the meaning of ",input_word,"is: ",a[input_word]);
else:
      print("the word is not in the dictionary");
      