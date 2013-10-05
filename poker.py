def poker(hands):
    """
   ([hand, hand, ...])-> hands
   Return the best hand from list of hands
   """
    return allmax(hands)
def allmax(hands):
    winhand = max(hands, key=hand_rank)
    maxval = hand_rank(winhand)
    return [hand for hand in hands if hand_rank(hand)==maxval]
def hand_rank(hand):
    """
    (hand)-> int
    Return the hand rank of a hand
    """
    ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
    ranks.sort(reverse=True)
    if ranks == [14,5,4,3,2]:
        ranks = [5,4,3,2,1]
        
    if straight_flush(hand):
        return 8, max(ranks)
    elif kind(4, ranks):
        return 0
def straight_flush(hand):
    """
    (hand)-> Bool

    Return True if hand is straight_flush,
    False otherwise
    """
    return straight(hand) and flush(hand)
def straight(hand):
    """
    (hand)-> Bool

    Return True if hand is straight,
    false otherwise
    """

    ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
    ranks.sort(reverse=True)
    if ranks == [14,5,4,3,2]:
        ranks = [5,4,3,2,1]
        
    return max(ranks)-min(ranks) == 4 and len(set(ranks)) == 5
def flush(hand):
    """
    (hand)-> Bool

    Return True if hand is flush, False otherwise.
    """
    
    suits = [s for r,s in hand]

    return len(set(suits)) == 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
