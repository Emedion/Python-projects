class Human:
    def __init__(self, name):
        self.name = name

    def stand(self):
        print(f"{self.name} stands")

class Person(Human):
    def talk(self):
        print(f"{self.name} Talks")


john = Person("John Ayelose")
john.talk()
john.stand()