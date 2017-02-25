import random
def whoWon(playerNum,dealerNum):
    if((21-playerNum)<(21-dealerNum)):
        return("player")
    else:
        return("dealer")
def genUnshuffledCards():
    cardNumbers=['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    cardSuites=['Spades','Clubs','Hearts','Diamonds']
    unshuffledDeck=['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
    #print(len(unshuffledDeck))
    k=0
    for i in cardSuites:
        for j in cardNumbers:
            unshuffledDeck[k]=str(j)+' of '+str(i)
            #print(k)
            k=k+1
    return(unshuffledDeck)
def shuffleDeck(deckOfCards):
    shuffledDeck=['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
    m=0
    for card in deckOfCards:
        for n in range(52):
            m=random.randint(0,51)
            if(shuffledDeck[m]==''):
                shuffledDeck[m]=card
                break
            else:
                m=random.randint(0,51)
    return(shuffledDeck)
def findCardValue(card):
    value=0
    if 'Ace' in card:
        value=11
    elif '2' in card:
        value=2
    elif '3' in card:
        value=3
    elif '4' in card:
        value=4
    elif '5' in card:
        value=5
    elif '6' in card:
        value=6
    elif '7' in card:
        value=7
    elif '8' in card:
        value=8
    elif '9' in card:
        value=9
    else:
        value=10
    return(value)
print('Please note: this is a basic BlackJack game. For simplicity, All ace cards have the value of eleven')
doYouWantToPlay='y'
deckOfCards=genUnshuffledCards()
print('This is your unshuffled deck:')
for elem in deckOfCards:
    print(elem)
while (doYouWantToPlay=='y'):
    winner=''
    doYouWantToShuffleCards=str(input("Do you want to shuffle the cards? Enter the letter y for yes and the letter n for no: "))
    if (doYouWantToShuffleCards=='y'):
        deckOfCards=shuffleDeck(deckOfCards)
        print('Cards have been shuffled')
    elif (doYouWantToShuffleCards=='n'):
        print('Cards have not been shuffled. Carry on playing')
    else:
        print('Please enter either "y" or "n": ')
        doYouWantToShuffleCards=str(input("Do you want to shuffle the cards? Enter the letter y for yes and the letter n for no"))
        if (doYouWantToShuffleCards=='y'):
            deckOfCards=shuffleDeck(deckOfCards)
            print('Cards have been shuffled')
        elif (doYouWantToShuffleCards=='n'):
            print('Cards have not been shuffled. Carry on playing')
    print("Your cards: ")
    playerCardCount=0
    dealerCardCount=0
    print(deckOfCards[0])
    playerCardCount=playerCardCount+findCardValue(deckOfCards[0])
    print(deckOfCards[1])
    playerCardCount=playerCardCount+findCardValue(deckOfCards[1])
    print("Your card count is "+str(playerCardCount))
    n=2
    while (playerCardCount<22):
        hitOrStay=input("Hit or Stay(Enter 'hit' or 'stay')")
        if (hitOrStay=='stay'):
            break
        if (hitOrStay=='hit'):
            print(deckOfCards[n])
            playerCardCount=playerCardCount+findCardValue(deckOfCards[n])
            n=n+1
            print("Your card count is "+str(playerCardCount))
    print('Your final card count is '+str(playerCardCount))
    if (playerCardCount>21):
        #print("You lost")
        winner='dealer'
    print("Now the dealer's Turn")
    while (dealerCardCount<22):
        if((dealerCardCount+findCardValue(deckOfCards[n]))<22):
            print(deckOfCards[n])
            dealerCardCount=dealerCardCount+findCardValue(deckOfCards[n])
            print("Dealer card count is "+str(dealerCardCount))
            n=n+1
        else:
            break
    print("Dealer's final card count is "+str(dealerCardCount))
    if (winner!='dealer'):
        winner=whoWon(playerCardCount,dealerCardCount)
        if(winner=='dealer'):
            print("You lost")
        else:
            print("You won")
    elif(winner=='dealer'):
        print('You lost')
    doYouWantToPlay=input('Do you want to play again? Enter "y" or "n": ')
