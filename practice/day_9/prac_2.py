import random 

def game():
           print("guess the number is the game  ......")
           name = input("enter your name : ")
           score =0
           num = random.randint(1,10)
           while True:
            n = int(input("enter a number :"))
            if n == num:
                    print("right guess")
                    score = score+1
                    print("new score " + str(score))
                    with open("high_score","a") as f:
                            f.write(name +"\n score is : " + str(score)+ " \n")

                    break
            else:
                    print("wrong ans")
                    score = score - 1
                    print(name +"\n new score " + str(score))

game()
