import allfunctions
from allfunctions import *
#function makes a list of score of the combinations in the given combinationlist
#function takes in the parameters score(a list) and combinationlist(a list of combination(list which conatins three cards) of cards)
#def priority(score,combinationlist):
#function makes a list of all combinations possible from a given deck and gives it in combinationlist(a list of combination(list which conatins three cards) of cards)
#function takes in the parameters deck(list of cards) and combinationlist(list in which combinations are to be made or teh list of combinations)
#def combinationlist(deck,combinationlist):
print("Enter your cards:-")
card1=input('Card1:')
card2=input('Card2:')
card3=input('Card3:')
selection=[card1,card2,card3]
mycombinationlist=[[]]
for card in selection:
        if (card.startswith('s')):
            if (len(card)==3):
                mycombinationlist[0].append(deck[10+int(card[2])])
            else:
                mycombinationlist[0].append(deck[int(card[1])])
        elif (card.startswith('h')):
            if (len(card)==3):
                mycombinationlist[0].append(deck[23+int(card[2])])
            else:
                mycombinationlist[0].append(deck[13+int(card[1])])
        elif (card.startswith('c')):
            if (len(card)==3):
                mycombinationlist[0].append(deck[36+int(card[2])])
            else:
                mycombinationlist[0].append(deck[26+int(card[1])])
        elif (card.startswith('d')):
            if (len(card)==3):
                mycombinationlist[0].append(deck[49+int(card[2])])
            else:
                mycombinationlist[0].append(deck[39+int(card[1])])
myscorelist=list()
priority(myscorelist,mycombinationlist)
myscore=round(myscorelist[0],2)
mycards=mycombinationlist[0]
lst=list()
for card in mycards:
    for x in range(53):
        if (card.cardnumber==deck[x].cardnumber):
            lst.append(deck[x])
for y in lst:
    deck.remove(y)
combinationlist=[0]
allscore=list()
formlist(deck,combinationlist)
priority(allscore,combinationlist)
allscore.sort()
position=None
for score in allscore:
    if (myscore>score):
        continue
    else:
        position=allscore.index(score)
        break
players=input("Enter the number of players: ")
chance=(1-(probability((18424-position)/18424,(int(players)-1))))*100
print('Winning probability:',chance,'%')
