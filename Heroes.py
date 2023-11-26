import random
from Items import Heals, SmallPot, LargePot, Equipment, FlamingAxe

################################################## HERO ######################################################
class Hero:

    def __init__(self,Name):
        self.Class = "Hero"
        self.Name = Name
        OriginalHP = random.randint(20,30)
        self.OriginalHP = OriginalHP
        self.HP = self.OriginalHP
        self.MaxDMG = 10
        self.Gold = 0
        self.Inventory = []

    def GetName(self):
        return self.Name

    def getHP(self):
        return self.HP

    def getGold(self):
        return self.Gold

    def setMaxDMG(self,DMGAdd):
        self.MaxDMG += DMGAdd

    def AddToInv(self,Item):
        self.Inventory.append(Item)

    def PrintInv(self):
        if not self.Inventory:
            print("\nYour inventory is empty.") 
        else:
            for i in range(len(self.Inventory)):
                object=self.Inventory[i]
                print("Your inventory:\n\n\t")
                print("\n" +str(i+1) + ") " + str(object.getName()))

    def Attack(self):
        DMG = random.randint(0,self.MaxDMG)
        return DMG

    def Heal(self,Heal):
        if self.HP + Heal > self.OriginalHP:
            print("You cannot use that! You have too much health.")
        else:    
            self.HP += Heal 

    def TakeDMG(self,DMG):
        self.CurrentHP -= DMG

    def Purchase(self,Cost,Item,Name):
        if self.getGold() >= Cost:
            self.Gold -= Cost
            print("You stow the " + str(Name) + " in your bag.")
            self.AddToInv(Item)
        else:
            print("You do not have enough Gold to buy this item!")

#######################################################################################################################

################################################### CLERIC ####################################################

class Cleric(Hero):
    
    def __init__(self,Name):
        self.Class = "Cleric"
        self.Name = Name
        self.OriginalHP = random.randint(25,35)
        self.HP = self.OriginalHP
        self.MaxDMG = 8
        self.Gold = 0
        self.Inventory = []
        
#######################################################################################################################

################################################### WIZARD ####################################################

class Wizard(Hero):

    def __init__(self,Name):
        self.Class = "Wizard"
        self.Name = Name
        self.OriginalHP = random.randint(15,25)
        self.HP = self.OriginalHP
        self.MaxDMG = 15
        self.Gold = 0
        self.Inventory = []
        
#######################################################################################################################




































