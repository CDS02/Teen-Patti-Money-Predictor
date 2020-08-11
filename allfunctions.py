import cards
import math
from cards import *
#function makes a list of score of the combinations in the given combinationlist
#function takes in the parameters score(a list) and combinationlist(a list of combination(list which conatins three cards) of cards)
def priority(score,combinationlist):
    for combination in combinationlist:
        if(combination==0):
            continue
        combination.sort(key=lambda combination:combination.num)
        if ((combination[0].num==combination[1].num)&(combination[1].num==combination[2].num)):
            score.append(100000*combination[2].num)
        elif (((combination[2].num-combination[1].num==1)&(combination[2].num-combination[0].num==2))&((combination[1].suit==combination[0].suit)&(combination[1].suit==combination[2].suit))):
            score.append(10000*combination[2].num)
        elif ((combination[2].num==14)&(combination[1].num==3)&(combination[0].num==2)&(combination[1].suit==combination[2].suit)&(combination[1].suit==combination[0].suit)):
            score.append((10000*combination[2].num)-1)
        elif ((combination[2].num-combination[1].num==1)&(combination[2].num-combination[0].num==2)):
            score.append(1000*combination[2].num)
        elif ((combination[2].num==14)&(combination[1].num==3)&(combination[0].num==2)):
            score.append((1000*combination[2].num)-1)
        elif ((combination[2].suit==combination[1].suit)&(combination[1].suit==combination[0].suit)):
            score.append((100*combination[2].num)+(10*combination[1].num)+(combination[0].num))
        elif (combination[2].num==combination[1].num):
            score.append((20*combination[1].num)+combination[0].num)
        elif (combination[0].num==combination[1].num):
            score.append((20*combination[1].num)+combination[2].num)
        else:
            score.append((combination[2]).num+(.1*combination[1].num)+(.01*combination[0].num))
#function makes a list of all combinations possible from a given deck and gives it in combinationlist(a list of combination(list which conatins three cards) of cards)
#function takes in the parameters deck(list of cards) and combinationlist(list in which combinations are to be made or teh list of combinations)
def formlist(deck,combinationlist):
    rawelementlist=list()
    for card1 in deck:
        if (card1.cardnumber==0):
            continue
        combination=list()
        combination.append(card1)
        for card2 in deck:
            if (card2.cardnumber==0):
                continue
            if (card2.cardnumber<=card1.cardnumber):
                continue
            combination.append(card2)
            for card3 in deck:
                if (card3.cardnumber==0):
                    continue
                if (card3.cardnumber<=card2.cardnumber):
                    continue
                combination.append(card3)
                if (len(combination)==3):
                    rawelementlist.extend(combination)
                    del combination[2]
            del combination[1]
        del combination[0]
    combination=list()
    a=0
    combination.append(0)
    b=3
    z=int(len(rawelementlist)/3)
    for x in range((z+1)):
        if(x==0):
            continue
        combination.append(list())
        for y in range(a,b):
            combination[x].append(rawelementlist[y])
        a=a+3
        b=b+3
        combinationlist.append(combination[x])
#gives probability of even one success(even one player winning)
def probability(winning,players):
    successprobability=1-pow((1-winning),players)
    return successprobability
