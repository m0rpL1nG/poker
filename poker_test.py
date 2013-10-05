import unittest
import poker
class Testpoker(unittest.TestCase):
    '''Example unittest test methods for poker. [Return the hand rank of a hand]'''
    def test_poker(self):
    	'''Test test_poker with sf = ['JC', 'TC', '9C', '8C', '7C'] And sf2 = ['JS', 'TS', '9S', '8S', '7S'] '''
    	sf = ['JC', 'TC', '9C', '8C', '7C']
    	actual = poker.poker(sf)
        expected = ['JC', 'TC', '9C', '8C', '7C']
        self.assertEqual(actual, expected)

        
    def test_hand_rank(self):
        '''Test hand_rank with sf = ['JC', 'TC', '9C', '8C', '7C']'''
        sf = ['JC', 'TC', '9C', '8C', '7C']
        actual = poker.hand_rank(sf)
        expected = 8, 11 
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)