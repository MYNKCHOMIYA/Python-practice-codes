class train():
      available_seats= 90
      fare = 560

      @staticmethod
      def greet():
       print("welcome to indian railways") 

      @staticmethod 
      def get_status():
            print(f"available_seats = {train.available_seats}")
      
      @staticmethod
      def get_fare():
            print(f"the fare of tarin per seat is : Rs.{train.fare}")
      
      @staticmethod
      def book():
       print("booking ticket")
       seat = int(input("enter the number of seat u need : "))
       if seat <= train.available_seats:
                 print("seat is available")
                 print(f"total fare = {train.fare*seat}")
                 name = input("enter your name : ")
                 train.available_seats -= seat
                 print("payment done")
                 print(f"{seat} is booked by the name of {name}")
       else:
                  print("seat is unavailable")
      
          
train.greet()
train.get_status()
train.get_fare()
train.book()
train.get_status()
      