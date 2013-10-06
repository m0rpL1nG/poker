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
#    elif fullhouse(hand):
#        return 6
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
    pass


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