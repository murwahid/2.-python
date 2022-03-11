class Pet:
    # implement __init__( name , type , tricks ):
    def __init__(self,name,type,tricks,health,energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
# sleep() - increases the pets energy by 25 
    def sleep(self):
        self.energy += 25 
# eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy +=5 
        self.health +=10
        print(f"{self.name} has increased energy! Energy: {self.energy} ")
# play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        print(f"{self.name} has increased by 5")
# noise() - prints out the pet's sound
    def noise(self):
        print(f"{self.name} goes Woof!")

class Ninja():
# implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name,last_name,treats,pet_food,pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        return self
# feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        self.pet.eat()
        return self
# # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.bathe()
        return self

class Fish(Pet):
    # implement __init__( name , type , tricks ):
    def __init__(self,name,type,tricks,health,energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
# sleep() - increases the pets energy by 25 
    def swim(self): 
        print(f"Fish is swimming")
    






pet_1 = Pet("zara", "doggie", "Penguin", 80, 60)
pet_2 = Pet("Dole", "dog","bark",100,15)
fish = Fish("Goldie", "fish", "jump", 100,100)
moose = Ninja("Musashi", "Miyamoto", "Apples", "kibbles", pet_2)

moose.walk()
fish.eat()