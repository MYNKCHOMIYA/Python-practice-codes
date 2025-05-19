f = open("poems.txt","r")
content = f.read()
if "twinkle" in content:
      print("file has poem")
else:
      print("it does not have any kind of poem")
f.close()







