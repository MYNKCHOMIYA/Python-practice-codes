with open("donkey.txt","r") as f:
      content = f.read()
      g= content.count("donkey")
     
with open("donkey.txt","w") as k:

      h= content.replace("donkey","######")
      w = k.write(h)

      print(g)

      