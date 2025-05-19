def cal(x):
      if x == 0:
            return 0
      else:
            return x + cal(x - 1)

x = int(input("enter the number: "))
total_sum = cal(x)
print(total_sum)