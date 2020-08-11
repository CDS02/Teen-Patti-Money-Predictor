class cards:
    def __init__(self,number,suit):
        self.num=number
        self.suit=suit
    num=0
    suit=None
    cardnumber=0
suitlist=('Spades','Hearts','Clubs','Diamonds')
numlist=(14,2,3,4,5,6,7,8,9,10,11,12,13)
deck=list()
a=cards(0,None)
deck.append(a)
a.cardnumber=0
for suit in suitlist:
    for number in numlist:
        deck.append(cards(number,suit))
number=1
for card in deck:
    if (card.num==0):
        continue
    card.cardnumber=number
    number=number+1
