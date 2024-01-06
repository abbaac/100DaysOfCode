class Animal:
    def __init__(self):
        self.eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water")

dog = Animal()
fish = Fish()

dog.breathe()

fish.breathe()
fish.swim()