# Import



# Classes

class Card:

    def __init__(self, strName, strTxt, intManaCost):

        self.__name = strName
        self.__txt = strTxt
        self.__manaCost = intManaCost

    def getName(self):
        return self.__name
    
    def getTxt(self):
        return self.__txt
    
    def getManaCost(self):
        return self.__manaCost

class Crystal(Card):

    def __init__(self, strName, strTxt, intManaCost, intValue):
        super().__init__(strName, strTxt, intManaCost)

        self.__value = intValue

    def getValue(self):
        return self.__value
    
    def use(self, target):
        target.__totalMana += self.__value

class Creature(Card):

    def __init__(self, strName, strTxt, intManaCost, intHp, intAtk):
        super().__init__(strName, strTxt, intManaCost)

        self.__hp = intHp
        self.__atk = intAtk

    def getHp(self):
        return self.__hp
    
    def getAtk(self):
        return self.__atk
    
    def loseHp(self, atk):

        self.__hp -= atk

    def isAlive(self):

        if self.__hp <= 0:
            return False
        
        return True

class Blast(Card):

    def __init__(self, strName, strTxt, intManaCost, intValue):
        super().__init__(strName, strTxt, intManaCost)

        self.__value = intValue

    def getValue(self):
        return self.__value
    
    def use(self, target):

        target.__hp -= self.__value

class Mage:

    def __init__(self, strName):

        self.__name = strName
        self.__hp = 30
        self.__totalMana = 2
        self.__currentMana = self.__totalMana
        self.__currentCard = [Crystal("Mana Crystal","Increase your maximum mana by 1",0,1),
                              Crystal("Refined Mana Crystal","Increase your maximum mana by 2",2,1),
                              Creature("Goblin","A weak but heinous little green guy",2,3,4),
                              Creature("Dragon","A magnificient red scaled dragon",5,10,6),
                              Blast("Fireball","Deal 2 damages to anyone",3,2)]
        self.__usedCard = []
        self.__playedCard = []

    def getName(self):
        return self.__name
    
    def getHp(self):
        return self.__hp
    
    def getCurrentMana(self):
        return self.__currentMana
    
    def getTotalMana(self):
        return self.__totalMana
    
    def getListCurrentCard(self):
        return self.__currentCard
    
    def getListUsedCard(self):
        return self.__usedCard
    
    def getListPlayedCard(self):
        return self.__playedCard
    
    def play(self, nbrCard):

        if self.__currentMana >= self.__currentCard[nbrCard].getManaCost():
            self.__playedCard.append(self.__currentCard[nbrCard])
            self.__currentCard.pop(nbrCard)
            self.__currentMana -= self.__currentCard[nbrCard].getManaCost()
            return True

        else:
            print("You don't have enough mana")
            return False


    def increaseMana(self):

        self.__currentMana = self.__totalMana

    def attack(self, target, nbrCard):

        target.__hp -= self.__playedCard[nbrCard].getAtk()

# Functions



# Variables



# Main Code

choiceName = str(input("Choose a name\n\n"))

player = Mage(choiceName)
opponent = Mage("Jenna")

print(f"\nWelcome {player.getName()}, you will now fight against {opponent.getName()}\n\nGood luck !\n")

while player.getHp() > 0 and opponent.getHp() > 0:

    # Boucle de jeu à incrémenter pour 2 joueurs

    print("")
    print("")
    for i in range(len(opponent.getListPlayedCard())):
        print(f"[{opponent.getListPlayedCard()[i].getName()}]", end="")
    print("")
    for j in range(len(player.getListPlayedCard())):
        print(f"[{player.getListPlayedCard()[j].getName()}]", end="")

    choiceCard = 10
    choiceList = []

    for k in range(len(player.getListCurrentCard())):
        choiceList.append(k+1)
    
    while choiceCard not in choiceList :

        print(f"\nWhat do you want to play ?\n")

        for l in range(len(player.getListCurrentCard())):
            print(f"{l+1} - {player.getListCurrentCard()[l].getName()} - {player.getListCurrentCard()[l].getTxt()} - Mana cost : {player.getListCurrentCard()[l].getManaCost()}")
        print(f"{l+2} - Pass your turn")

        choiceCard = int(input("\n"))

        if choiceCard not in choiceList:
            print("Not a valid choice")

    player.play(choiceCard-1)

    # Utilisation de la carte ou choix attaque avec monstre sur terrain de jeu
    
