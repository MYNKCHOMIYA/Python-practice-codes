def temp(CEL):
        FAR = (CEL * 9/5) + 32
        return FAR
      

CEL = int(input("Enter temperature in Celsius: "))
far = temp(CEL)
print("Temperature in Fahrenheit is: ",far)