from Person import Person

Person1 = Person("Daniel",age,steps)
Person2 = Person("Nora",age,steps)

print(Person1.getName() + " is " + str(Person1.getAge()) + " years old.")

ValidInput = True

while ValidInput == True:
    Action = int(input("What do you want to do?:\n1. Walk.\n2. Talk\n"))
    if Action == 1:
        pass
