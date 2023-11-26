class Person:

    def __init__(self,name,age,steps):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def setName(self):
        self.name = name

    def setAge(self):
        self.age = age

    def walk(self,steps):
        message = self.name + " walks " + steps + " steps."
        print(message)

    def talk(self,message):
        Talk = self.name + " says " + message
        print(Talk)
