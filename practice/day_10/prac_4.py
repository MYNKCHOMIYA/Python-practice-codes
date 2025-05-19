a = int(input("enter a number : "))
class cal():
      cube = a*a*a
      square = a*a
      square_root = a**.5
      @staticmethod
      def greet():
            print("hello")

cal.greet()
num = cal()
print(f"cube = {num.cube},\nsquare = {num.square},\nsquare root = {num.square_root}")



