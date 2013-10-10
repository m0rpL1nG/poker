def poker(hands):
    """
    
    Return the best hand from list of hands

    """
    return allmax(hands)

def allmax(hands):
    winhand = max(hands, key=hand_rank)
    maxval = hand_rank(winhand)
    result = []
    for hand in hands:
        if hand_rank(hand) == maxval:
            result.append(hand)
    return result

def hand_rank(hand):
    """
    hand -> int

    Return the hand rank of a hand
    """
    if straight_flush(hand)[0]:
        return 8,straight_flush(hand)[1]
    elif kind(hand,4):
        return 7
    elif kind(hand,3) and kind(hand,2):
        return 6
    elif flush(hand):
        return 5
    elif straight(hand)[0]:
        return 4,straight(hand)[1]
    elif kind(hand,3):
        return 3
    elif twopair(hand):
        return 2
    elif kind(hand, 2):
        return 1
    else:
        return 0


def straight_flush(hand):
    """
    hand -> Bool

    Return True if hand is straight flush
    False otherwise
    """
    if straight(hand)[0] == True and flush(hand) == True :
        return True,straight(hand)[1]
    return False

def flush(hand):
    """
    hand -> Bool

    Return True if hand is flush
    False otherwise
    """
    box = []
    for i in hand:
        box.append(i[1])
    return box[0] == box[1] == box[2] == box[3] == box[4]

def straight(hand):
    """
    hand -> Bool

    Return True if hand is straight
    False otherwise
    """
    lis = '-23456789TJQK'
    rank = []
    for i in hand:
        if i[0] == 'A':
            rank.append(0)
            rank.append(13)
        for j in lis:
            if i[0] == j:
                rank.append(lis.index(j))
    rank.sort()
    if rank[0]+1 == rank[1] and rank[1] +1 == rank[2] and rank[2]+1 == rank[3] and rank[3]+1 == rank[4]:
        return True,max(rank)
    return False

#def four_of_a_kind(hand):
#    """
#    hand -> Bool
#
#    Return True if hand is four of a kind
#    False otherwise
#    """
#    rank =[]
#    cardindex = '--23456789TJQKA'
#    for r,s in hand:
#        rank.append(cardindex.index(r))
#    rank.sort()
#    for r in rank:
#        if rank.count(r) == 4:
#            return True
#    return False


#def full_house(hand):
#    """
#    hand -> Bool
#
#    Return True if hand is full house
#    False otherwise
#    """
#    i = 0
#    rank = []
#    counted = []
#    cardindex = '--23456789TJQKA'
#    for r,s in hand:
#        rank.append(cardindex.index(r))
#    rank.sort()
#    for r in rank:
#        if rank.count(r) == 3 or rank.count(r) == 2:
#            if r not in counted:
#                i += 1
#                counted.append(r)
#    if i == 2:
#        return True
#    return False


#def onepair(hand):
#    """
#    hand -> Bool

#    Return True if hand is onepair
#    False otherwise
#    """
#    rank =[]
#    cardindex = '--23456789TJQKA'
#    for r,s in hand:
#        rank.append(cardindex.index(r))
#        if rank.count(int(r)) == 2 :
#            return True
#    return False

def twopair(hand):
    """
    hand -> Bool

    Return True if hand is twopair
    False otherwise
    """
    rank =[]
    cardindex = '--23456789TJQKA'
    for r,s in hand:
        rank.append(cardindex.index(r))
    if len(set(rank)) == 3 :
        return True
    return False


#def three_of_a_kind(hand):
#    """
#    hand -> Bool
#
#    Return True if hand is three of a kind
#    False otherwise
#    """
#    rank =[]
#    cardindex = '--23456789TJQKA'
#    for r,s in hand:
#        rank.append(cardindex.index(r))
#    rank.sort()
#    for r in rank:
#        if rank.count(r) == 3:
#            return True
#    return False


def kind(hand,n):
    """
    hand -> Bool

    Return True if hand is n kind
    False otherwise
    """
    rank =[]
    cardindex = '--23456789TJQKA'
    for r,s in hand:
        rank.append(cardindex.index(r))
    rank.sort()
    for r in rank:
        if rank.count(r) == n:
            return True
    return False
