with open("log.txt","r") as f:
     content= f.read()
     if "Python" in content :
          print("python is contained in  log.txt")
     else:
          print("phython is not available in log.txt")