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
        return 7,kind(hand,4)
    elif kind(hand,3) and kind(hand,2):
        return 6,kind(hand,3)
    elif flush(hand)[0]:
        return 5,flush(hand)[1]
    elif straight(hand)[0]:
        return 4,straight(hand)[1]
    elif kind(hand,3):
        return 3,kind(hand,3)
    elif twopair(hand):
        return 2, twopair(hand)[0], twopair(hand)[1]
    elif kind(hand, 2):
        return 1,kind(hand,2)
    else:
        return 0


def straight_flush(hand):
    """
    hand -> Bool

    Return True if hand is straight flush
    False otherwise
    """
    if straight(hand)[0] and flush(hand)[0]:
        return True,straight(hand)[1]
    return False,0

def flush(hand):
    """
    hand -> Bool

    Return True if hand is flush
    False otherwise
    """
    li = '-23456789TJQKA'
    ranks = []
    box = []
    for i in hand:
        box.append(i[1])
        for j in li:
            if i[0] == j:
                ranks.append(li.index(j))
    ranks.sort(reverse=True)
    return box[0] == box[1] == box[2] == box[3] == box[4],ranks


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
    return False,0

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
    high_pair = 0
    low_pair  = 0
    for r,s in hand:
        rank.append(cardindex.index(r))
    rank.sort(reverse=True)
    for r in rank:
        if rank.count(r) == 2:
            high_pair =  r
    rank.sort()
    for r in rank:
        if rank.count(r) == 2:
            low_pair =  r
    if high_pair != low_pair:
        return (high_pair, low_pair)
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
    hand -> int

    Return r if hand is n kind
    0 otherwise
    """
    rank =[]
    cardindex = '--23456789TJQKA'
    for r,s in hand:
        rank.append(cardindex.index(r))
    rank.sort()
    for r in rank:
        if rank.count(r) == n:
            return r
    return 0
