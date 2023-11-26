from Monster import Monster, Goblin, Vampire, Orc
from Heroes import Hero, Cleric, Wizard
from Items import Heals, SmallPot, LargePot, Equipment, FlamingAxe
import random

############################################################ Subroutines ############################################################

def RandomColour(): #Chooses a colour at random for the monster 
    ColourList = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
    Colour = ColourList[random.randint(0, (len(ColourList)-1))]
    return Colour



def Combat(HeroHP,Monster): #Does combat between monster and hero
    while HeroHP > 0 and MyMonster.getHP() > 0: #Continues until either is dead
        print("\n##### Hero: " + str(HeroHP) + " HP ##### Monster: " +
              str(MyMonster.getHP()) + " HP #####\n") #Prints hero and monster HPs

        AnyKey = input("Press enter to attack!: ") #Gets user to attack

        MyMonster.receiveDMG(theHero.Attack()) #Deals damage to monster

        if MyMonster.getHP() > 0: #Only lets monster attack if HP is above 0
            print("The " + MyMonster.getSpecies() + " attacks!") #Gets user to defend against attack
            AnyKey = input("Press enter to defend!: ")
            HeroHP -= MyMonster.attack() #Subtracts monster damage from player's health
    return HeroHP


def ChooseMonster(): #Chooses the monster type and colour
    MonsterChoice = random.randint(0,3)
    if MonsterChoice == 0:
        MyMonster = Monster(RandomColour())
    elif MonsterChoice == 1:
        MyMonster = Goblin(RandomColour())
    elif MonsterChoice == 2:
        MyMonster = Vampire(RandomColour())
    elif MonsterChoice == 3:
        MyMonster = Orc(RandomColour())
    return MyMonster


def FirstLetterVowel(Word): #Checks if first letter in word is a vowel
    Vowels = ["a","e","i","o","u"]
    VowelFound = False
    for i in range(len(Vowels)):
        if Word[0] == Vowels[i]:
            VowelFound = True
            break
        else:
            VowelFound = False
    return VowelFound


def Encounter(Colour,Species): #Prints encounter message
    if FirstLetterVowel(Colour) == True:
        print("\nYou are attacked by an " + Colour + " " + Species + "!")
    else:
        print("\nYou are attacked by a " + MyMonster.getColour() + " " + MyMonster.getSpecies() + "!")
            

def ChooseClass(): #Gives user description of classes and lets them choose
    ValidInput = False 
    while ValidInput == False:
        Name = str(input("What is your name, challenger?: ")) #Gets Name
        if Name == "":
            print("You need to put something! Try again.")
        else:
            ValidInput = True
    ValidInput = False 
    while ValidInput == False: #Loops until valid input
        print("\t\nWhat is your manner of combat, " + Name + "? (Choose 1, 2, or 3):\n")
        print("\t1) Hero: 20-30 HP. 0-10 ATK.") #Gives class options
        print("\t2) Cleric: 25-35 HP. 0-8 ATK.")
        print("\t3) Wizard: 15-25 HP. 0-15 ATK.")
        Choice = input("\nChoice: ")

        if Choice == "1": #Assigns class type to choice
            theHero = Hero(Name)
            ValidInput = True
        elif Choice == "2":
            theHero = Cleric(Name)
            ValidInput = True
        elif Choice == "3":
            theHero = Wizard(Name)
            ValidInput = True
        else: #Lets user try again if they put something other than 1, 2, or 3
            print("\nYou can only choose 1, 2 or 3. Please try again: ")
    return theHero


def Line(): #Prints out a line
    print("\n#######################################################################")

def MonsterDies(Victories): #Does all of the stuff associated with a monster dying
    Victories += 1
    MyMonster.die() #Prints monster death messages
    theHero.Gold += MyMonster.getGold() #Adds dropped gold to hero's gold
    if Victories == 3:
        return Victories #Stops if 3 monsters have been killed
    elif Victories < 3 and Victories != 1:
        AnyKey = input("\nYou are victorious! You have killed " + str(Victories) + " monsters so far. Press enter to fight the next monster, or if you would like to access your inventory, put 'e'.")
        AnyKey = AnyKey.upper()
        if AnyKey == "E":
            theHero.PrintInv()
        return Victories
    else:
        AnyKey = input("\nYou are victorious! You have killed " + str(Victories) + " monster so far. Press enter to fight the next monster, or if you would like to access your inventory, put 'e'.")
        AnyKey = AnyKey.upper()
        if AnyKey == "E":
            theHero.PrintInv()
        return Victories


def Shop(Gold):
    Cont = "Y"
    while Cont == "Y":
        print("\n#################### Welcome to Ye Olde Dungeon Shoppe! ####################")
        print("\nStock:")
        print("\t1) Small Potion: Heals 5 HP - 5 Gold")
        print("\t2) Large Potion: Heals 10 HP - 10 Gold")
        print("\t3) Flaming Axe: +5 Maximum DMG - 15 Gold")
        print("\t4) Exit shoppe")
        print("\nYour current gold is: " + str(theHero.getGold()))
        ValidInput = False 
        while ValidInput != True:
            Choice = input("\nSelect option: ")
            if Choice == "1":
                aSmallPot = SmallPot()
                theHero.Purchase(aSmallPot.getCost(),aSmallPot,aSmallPot.getName())
                ValidInput = True
                theHero.PrintInv()    
            elif Choice == "2":
                aLargePot = LargePot()
                theHero.Purchase(aLargePot.getCost(),aLargePot,aLargePot.getName())
                ValidInput = True
            elif Choice == "3":
                aFlamingAxe = FlamingAxe()
                theHero.Purchase(aFlamingAxe.getCost(),aFlamingAxe,aFlamingAxe.getName())
                ValidInput = True
            elif Choice == "4":
                Cont = "N"
                print("\nCome again soon!\n")
                ValidInput = True
            else:
                print("Invalid choice! Please try again.")
                
def ChoiceToPrintInv():
    ValidInput = False
    while ValidInput == False:
        Choice = input("Would you like to acces your inventory? (Y/N): ")
        Choice = Choice.upper()
        if Choice == "Y":
            theHero.PrintInv()
            ValidInput = True
        elif Choice == "N":
            print()
            ValidInput = True
        else:
            print("Invalid input. Please try again.")
    
    
        

############################################################ MAIN CODE ############################################################

print("#################### Welcome To Death Trap Dungeon! ####################\n") #Welcomes user

theHero = ChooseClass() #Chooses class
Victories = 0

while Victories < 3 and theHero.getHP() > 0: #Plays until either hero dies or wins 3 fights
    
    Line() #Prints out a line to separate the battle
    MyMonster = ChooseMonster() #Chooses monster type and colour
    Encounter(MyMonster.getColour(),MyMonster.getSpecies()) #Prints encounter message
    theHero.HP = Combat(theHero.HP,Monster) #Does combat between Monster and Hero 

    if theHero.getHP() > 0: #If hero is still alive, adds 1 victory, kills monster, starts next fight
        Victories = MonsterDies(Victories)
        Shop(theHero.getGold())
    else: #If hero is dead, ends game
        print("The Death Trap Dungeon claims another victim. You are dead.") 

if Victories == 3: #If 3 monsters have been killed
    print("\nYou succesfully killed 3 monsters in single combat! You Win!\n")
    print("You leave the dungeon with " + str(theHero.getGold()) + " gold.") #Prints gold collected 
    theHero.PrintInv()
    print("############################## GAME OVER ##############################")
    

    
