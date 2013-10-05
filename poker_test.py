import unittest
import poker
class Testpoker(unittest.TestCase):
    '''Example unittest test methods for hand_rank. [Return the hand rank of a hand]'''
    def test_poker(self):
    	'''Test hand_rank with sf = ['JC', 'TC', '9C', '8C', '7C']'''
    	sf = ['JC', 'TC', '9C', '8C', '7C']
    	sf2 = ['JS', 'TS', '9S', '8S', '7S']
    	actual = poker.poker([sf, sf2])
        expected = [['JC', 'TC', '9C', '8C', '7C'], ['JS', 'TS', '9S', '8S', '7S']]
        self.assertEqual(actual, expected)
    def test_hand_rank_straight_flush(self):
        '''Test hand_rank with sf = ['JC', 'TC', '9C', '8C', '7C']'''
        sf = ['JC', 'TC', '9C', '8C', '7C']
        actual = poker.hand_rank(sf)
        expected = 8, 11 
        self.assertEqual(actual, expected)





if __name__ == '__main__':
    unittest.main(exit=False)