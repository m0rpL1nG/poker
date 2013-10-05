def poker(hands):
    """
   ([hand, hand, ...])-> hands
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
    (hand)-> int

    Return the hand rank of a hand
    """
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()