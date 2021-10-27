class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print("talk")


test = Person("Emma")
print(test.name)
test.talk()