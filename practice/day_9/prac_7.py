with open("log.txt","r") as log:
      lines = log.readlines()
      for i, lines in enumerate(lines,start=1):
                  if "Python" in lines:
                        print("Python is present in lines :" )
                        print(f"line {i} :  {lines.strip()}")

            