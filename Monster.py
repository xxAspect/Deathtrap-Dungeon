import random

############################################################ MONSTER ############################################################
class Monster:

    def __init__(self,Colour):
        self.Colour = Colour
        self.species = "monster"
        self.HP = 10
        self.MaxDMG = 5
        self.AttackMessage = "It slashes with its sharp claws.\n"
        self.DeathMessage = "The monster keels over and dies, its wounds leaking blood onto the floor.\n"
        self.Gold = random.randint(1,10)
                                

    def getHP(self): #Gets HP of the monster
        return int(self.HP)

    def getColour(self): #Gets the colour of the monster
        return self.Colour

    def getSpecies(self): #Gets the Species of the monster
        return self.species

    def getGold(self):
        return self.Gold
    
    def die(self):
        print(self.DeathMessage + "The " + self.species + " drops " + str(self.Gold) + " gold.")
        
#returns damage monster inflicts and gives combat prompts to help visualise it
    def attack(self):
        damage = random.randint(0,self.MaxDMG)#gets the damage of the monster
        if damage == 0:
            print("\tYou dodged the attack! No damage!\n")
        elif damage == 1:
            print("\tA glancing blow! You receive 1 point of damage!\n")
        else:
            print("\n" + self.AttackMessage + "\tYou receive " + str(damage) + " points of damage!\n")
        return(damage)

#Subtracts damage from monster and prints related message
    def receiveDMG(self,damage):
        if damage == 0:
            print("\tYou missed! The " + self.species + " was too fast for you.\n")
        elif damage == 1:
            print("\tA glancing blow! The " + self.species + " takes 1 damage.\n")
        else:
            print("\tHit! The " + self.species + " takes " + str(damage) + " damage.\n")
        self.HP -= int(damage)
        
################################################################################################################################ 


############################################################ GOBLIN ############################################################
class Goblin(Monster):


    def __init__(self,Colour):
        self.Colour = Colour
        self.species = "goblin"
        self.HP = 11
        self.MaxDMG = 6
        self.AttackMessage = "It hits you with a club.\n"
        self.DeathMessage = "The goblin keels over and dies, its wounds leaking blood onto the floor.\n"
        self.Gold = random.randint(5,15)

################################################################################################################################# 


############################################################ VAMPIRE ############################################################
class Vampire(Monster):

    def __init__(self,Colour):
        self.Colour = Colour
        self.species = "vampire"
        self.HP = 12
        self.MaxDMG = 7
        self.AttackMessage = "The vampire makes a grab for your juicy neck and tries to sink its fangs into it.\n"
        self.DeathMessage = "The vampire lets out a bone-chilling scream before disintegrating.\n"
        self.Gold = random.randint(2,12)

################################################################################################################################# 


############################################################ ORC ################################################################
class Orc(Monster):

    def __init__(self,Colour):
        self.Colour = Colour
        self.species = "orc"
        self.HP = 11
        self.MaxDMG = 8
        self.AttackMessage = "The orc screams and swings his tree trunk adorned with spikes at you.\n"
        self.DeathMessage = "The orc lets out a final roar before falling to the ground and dying.\n"
        self.Gold = random.randint(10,15)











        
