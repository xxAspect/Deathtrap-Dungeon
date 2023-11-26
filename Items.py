
#################################################### HEALS ##########################################################
class Heals:

    def __init__(self):
        self.Name = ""
        self.HPRestore = 5
        self.Cost = 5

    def getName(self):
        return self.Name

    def getCost(self):
        return self.Cost

    def getHPRestore(self):
        return self.HPRestore

    def Heal(self,PlayerHP):
        PlayerHP += self.HPRestore
        print("You drink the " + self.Name + ". It tastes like mould, but it does the trick. + " + self.HPRestore + "HP.")
        return PlayerHP

#####################################################################################################################

################################################## SMALL POT ########################################################

class SmallPot(Heals):

  def __init__(self):
        self.Name = "Small Potion"
        self.HPRestore = 5
        self.Cost = 5

#####################################################################################################################

################################################## LARGE POT ########################################################

class LargePot(Heals):

    def __init__(self):
        self.Name = "Large Potion"
        self.HPRestore = 10
        self.Cost = 10

#####################################################################################################################

#####################################################################################################################

################################################## EQUIPMENT ########################################################

class Equipment:

    def __init__(self):
        self.Name = ""
        self.DMGAdd = 0
        self.Cost = 0

    def getName(self):
        return self.Name

    def getCost(self):
        return self.Cost

    def getDMGAdd(self):
        return self.DMGAdd

#####################################################################################################################

################################################## FLAMING AXE ######################################################

class FlamingAxe(Equipment):
    
    def __init__(self):
        self.Name = "Flaming Axe"
        self.DMGAdd = 5
        self.Cost = 15

    






























