"""
Week 14 Lecture script: Inheritance & Polymorphism
"""

#Check and set your current directory
import os
cwd=os.getcwd() #This is your current working directory
print cwd

import os
preferred_dir="C:\Users\Mujde\Documents\ISTANBUL_SEHIR_UNI" \
              "\ENGR 101_SPRING 2019_HMA\Week 14" #Please set yours properly
os.chdir(preferred_dir) #Now you have changed your working directory to your preferred directory
#as you defined above. Please set yours properly!
cwd=os.getcwd()
print cwd

#SLIDE 16
class Vehicle(object): #You need to write here: object
    flat_rate = 0
    wheels = 0
    def __init__(self, kilometers, make, model, year):
        """Return a new Vehicle object."""
        self.kilometers = kilometers
        self.make = make
        self.model = model
        self.year = year

    def sale_price(self):
        return 5000 * self.wheels

    def purchase_price(self):
        return self.flat_rate - (0.10 * self.kilometers)

    def vehicle_advertisement_text(self):
        return str(self.year) + ' ' + self.make + ' ' + \
               self.model + ' - ' + str(self.kilometers) + ' km'

class Car(Vehicle):
    flat_rate = 8000
    wheels = 4
    def vehicle_advertisement_text (self):
        return 'Car - ' + super(Car, self).vehicle_advertisement_text()

class Truck(Vehicle):
    flat_rate = 10000
    wheels = 10
    def vehicle_advertisement_text (self):
        return 'Truck - ' + super(Truck, self).vehicle_advertisement_text()

class Motorcycle(Vehicle):
    flat_rate = 4000
    wheels = 2
    def vehicle_advertisement_text(self):
        return 'Motorcycle-' + super(Motorcycle,self).vehicle_advertisement_text()


car = Car(30000, 'Toyota', 'Corolla', 2008) #kilometers, make, model, year
print car.vehicle_advertisement_text()
print car.purchase_price()

motorcycle = Motorcycle(30000, 'BMW', 'C400', 2018)
print motorcycle.vehicle_advertisement_text()
print motorcycle.purchase_price()

#SLIDE 18&19: Animal World
class Cat:
    def __init__(self, name):
        self.name = name

class Dog:
    def __init__(self, name):
        self.name = name

animals = [Cat('Missy'),
           Cat('Mistof'),
           Dog('Lassie')]

for a in animals:
  if isinstance(a, Cat):
    print a.name + ': ' + 'Meow'
  elif isinstance(a, Dog):
    print a.name + ': ' + 'Woof'

#SLIDE 21&22: POLYMORPHISM
class Animal(object):
    def __init__(self, name):
        self.name = name

    def talk(self):
        return 'what?'

class Cat(Animal):
    def talk(self):
        return 'Meow!'

class Dog(Animal):
    def talk(self):
        return 'Woof!'

animals = [Cat('Missy'),
           Cat('Mistof'),
           Dog('Lassie')]

for animal in animals:
    print animal.name + ': ' + animal.talk()

#SLIDE 24: Sum is a polymorphic function
class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    # # SLIDE 10
    def __str__(self):
        return str(self.hour) + ':' + str(self.minute) + ':' + str(self.second)

    def print_time(self):
        print str(self.hour) + ':' + str(self.minute) + ':'\
          + str(self.second)

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def int_to_time(self,seconds):
        hour = (seconds / 3600) % 24
        minute = (seconds /60) % 60
        second = seconds % 60
        return Time(hour, minute, second)

    def increment(self, seconds):
        tot_secs = seconds + self.time_to_int()
        return self.int_to_time(tot_secs)

    def is_after(self, other):
        return self.time_to_int() >other.time_to_int()


    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return self.int_to_time(seconds)

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    # SLIDE 18: Right side addition
    def __radd__(self, other):
        return self.__add__(other)

t1 = Time(7, 43)
t2 = Time(7, 41)
t3 = Time(7, 37)
print t1+t2+t3
total = sum([t1, t2,t3])
print total

print sum([1, 2, 3])
#Sum is a polymorphic function, it works both for integers and time objects

#SLIDE 25:
def histogram(s):
    d=dict()
    for c in s:
        if c not in d:
            d[c]=1
        else:
            d[c]=d[c]+1
    return d
my_string="banana"
my_list=["spam","egg","spam","spam","bread"]
my_tuple=("a","b","c","b","a","a","a","d")
#Histogram is a polymorphic function because it works for different types:
# strings, lists, tuples and even dictionaries.
print histogram(my_string)
print histogram(my_list)
print histogram(my_tuple)

#SLIDE 28:
class Card(object):
    """represents a standard playing card."""
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King']
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return Card.rank_names[self.rank] + ' of ' + \
               Card.suit_names[self.suit]

    #SLIDE 30: Operator overloading
    def __cmp__(self,other):
        # check the suits
        if self.suit > other.suit:
            return 1
        if self.suit < other.suit:
            return -1
        # suits are the same... check ranks
        if self.rank > other.rank:return 1
        if self.rank < other.rank:return -1

        # ranks are the same... it's a tie
        return 0

first_card=Card(0,3)
print first_card
second_card=Card(1,3)
print second_card
print first_card.__cmp__(second_card) #first card smaller
print first_card>second_card #first card smaller

#SLIDE 32: DECK: A deck of card
class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank) #create card object 13 times for each suit
                self.cards.append(card)

    # SLIDE 33
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res) #string elements of a sequence have been joined by '\n' separator.

    #SLIDE 34
    def pop_card(self):
        return self.cards.pop()
    
    #SLIDE 35
    def add_card(self, card):
        self.cards.append(card)

    # SLIDE 36
    def shuffle(self):
        import random
        random.shuffle(self.cards)
        return self.cards

    # SLIDE 43
    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())
        return hand

    # SLIDE 45
    def deal_hands(self, hand_num, card_num):
        hands = []
        for i in range(hand_num):
            hand = Hand('hand ' + str(i)) #Create a hand object
            self.move_cards(hand, card_num) #Add card_num times card to the add
            hands.append(hand) # a list of hands with hand_num elements (embedded lists)
        return hands


myDeck=Deck()
print myDeck
print myDeck.shuffle()
print myDeck.shuffle()[1]

#SLIDE 40
class Hand(Deck):
    """represents a hand of playing cards"""
    def __init__(self, label=''):
        self.cards = []
        self.label = label #new attribute

#SLIDE 41
hand = Hand('new hand')
print hand.cards #empty
print hand.label #new hand

#SLIDE 42
deck = Deck()
print deck

card = deck.pop_card() #pop one card
print card

hand = Hand('new hand') #restart a new hand
print hand.cards
hand.add_card(card) #add that card to the hand
print hand


card2 = deck.pop_card() #pop one more card
print card2

hand.add_card(card2) #add that card to the hand
print hand

#SLIDE 43
newhand = Hand('new hand') #restart a new hand
print newhand
print deck.move_cards(newhand,5)

#SLIDE 45
my_hands=deck.deal_hands(2, 7)
print my_hands
print my_hands[0]
print my_hands[1]

# Exercise 1

"""Write a class Game with attributes energy, money and no_of_castles, 
and a show_info (which will print the attributes’ values) method. 

Write a class named Player that will inherit from Game class and implement a create
_new_castle method which will allow the player to create a new castle if his energy is >5
 and his money is > 10, 
it should update the attributes accordingly. """

class Game(object):
    def __init__(self,money,no_of_castles,energy):
        self.energy=energy
        self.money=money
        self.no_of_castles=no_of_castles
    def show_info(self):
        print "Money amount is: ", str(self.money)
        print "Number of castles is: ", str(self.no_of_castles)
        print "Energy amount is: ", str(self.energy)

class Player(Game):
    def create_new_castle(self):
        if self.energy>5 and self.money>10:
            print "Creating a new castle"
            self.money=self.money-10
            self.energy=self.energy-5
            self.no_of_castles=self.no_of_castles+1
        else:
            print "Cannot create a new castle"
player1 = Player(30,60,10) #money,no_of_castles,energy
player1.show_info()

player1.create_new_castle()
player1.show_info()

#You cannot further create a new castle with the same player as left enegy is 5
player1.create_new_castle()
player1.show_info()

#Exercise 2
"""Create another class OponentPlayer that will inherit from class Game written before and 
it will have an additional attribute named no_of_destructions. 
Implement a method that will destroyCastle() which will allow the player
 to destroy a castle, thereby increasing his no_of_destructions attribute. 
 If the player’s energy is lower than 10, he won’t be able to destroy the castle."""

class OponentPlayer(Game):
    def __init__(self,money,no_of_castles,energy,no_of_destructions ):
        Game.__init__(self,money,no_of_castles,energy) #attributes as in parent Class game
        self.no_of_destructions =no_of_destructions

    def destroy_custle(self):
        if self.energy>10:
            print "destroying a castle"
            self.no_of_destructions =self.no_of_destructions+1
            self.energy=self.energy-10
            self.no_of_castles=self.no_of_castles-1
        else:
            print "You cannot destroy a castle with energy less than 10"

player2 = OponentPlayer(40, 30, 20, 30)
player2.show_info()

player2.destroy_custle()
player2.show_info()