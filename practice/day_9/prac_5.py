 #repeat program 4 for a list of such word to be censorceserd
censored = ["bsdk","madarchod","chutiya","gandu"]

with open("censor.txt","r") as f:
      content= f.read()
      count= 0
      for word in censored:
                         j= content.count(word)
                         count = count + j
                         content = content.replace(word,"####")
                        
                        

with open("censor.txt","w") as f:

      f.write(content)
print("count of censored item :" + str(count) +"\n")
print("after censor item is: \n"+ content)     
