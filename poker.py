def poker(hand):
    """
    hand -> int

    Return the hand rank of a hand
    """
    return hand_rank(hand)


def hand_rank(hand):
    """
    hand -> int

    Return the hand rank of a hand
    """
    if straight_flush(hand):
        return 8
    elif four_of_a_kind(hand):
        return 7
    elif fullhouse(hand):
        return 6
#    elif flush(hand):
#        return 5
#    elif straight(hand):
#        return 4
#    elif three_of_a_kind(hand):
#        return 3
#    elif twopair(hand):
#        return 2
#    elif onepair(hand):
#        return 1
#    else:
#        return 0


def straight_flush(hand):
    """
    hand -> Bool

    Return True if hand is straight flush
    False otherwise
    """
    if straight(hand) == True and flush(hand) == True :
        return True
    else:
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
    lis = '23456789TJQKA'
    rank = []
    for i in hand:
        for j in lis:
            if i[0] == j:
                rank.append(lis.index(j))
    rank.sort()
    if rank[0]+1 == rank[1] and rank[1] +1 == rank[2] and rank[2]+1 == rank[3] and rank[3]+1 == rank[4]:
        return True
    else :
        return False

def four_of_a_kind(hand):
    """
    hand -> Bool

    Return True if hand is four of a kind
    False otherwise
    """
    rank =[]
    cardindex = '--23456789TJQKA'
    for r,s in hand:
        rank.append(cardindex.index(r))
    rank.sort()
    for r in rank:
        if rank.count(r) == 4:
            return True
    return False


def full_house(hand):
    """
    hand -> Bool

    Return True if hand is full house
    False otherwise
    """
    i = 0
    rank = []
    counted = []
    cardindex = '--23456789TJQKA'
    for r,s in hand:
        rank.append(cardindex.index(r))
    rank.sort()
    for r in rank:
        if rank.count(r) == 3 or rank.count(r) == 2:
            if r not in counted:
                i += 1
                counted.append(r)
    print counted
    print i
    if i == 2:
        return True
    return False
