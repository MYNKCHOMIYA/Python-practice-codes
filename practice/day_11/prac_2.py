class animal():
 def sound(self):
    print("some gerenic sound it has")
class pet(animal):
    def play(self):
       print("playing with owerns")

class dog(pet):
    def bark(self):
     print("woof!, woof!")

Dog = dog()
Dog.sound()
Dog.play()
Dog.bark()

