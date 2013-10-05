import unittest
import poker
class Testpoker(unittest.TestCase):
    '''Example unittest test methods for poker. [Return the hand rank of a hand]'''
    def test_poker(self):
    	'''Test test_poker with sf = ['JC', 'TC', '9C', '8C', '7C'] And sf2 = ['JS', 'TS', '9S', '8S', '7S'] '''
    	sf = ['JC', 'TC', '9C', '8C', '7C']
    	sf2 = ['JS', 'TS', '9S', '8S', '7S']
    	actual = poker.poker([sf, sf2])
        expected = [['JC', 'TC', '9C', '8C', '7C'], ['JS', 'TS', '9S', '8S', '7S']]
        self.assertEqual(actual, expected)


    def test_hand_rank(self):
        '''Test hand_rank with sf = ['JC', 'TC', '9C', '8C', '7C']'''
        sf = ['JC', 'TC', '9C', '8C', '7C']
        actual = poker.hand_rank(sf)
        expected = 4, 11
        self.assertEqual(actual, expected)


    def test_straight(self):
    	'''Test straight with sf = ['JC', 'TC', '9C', '8C', '7C'] And fk = ['5S', '5H', '5D', '5C', 'KS']'''
        sf = ['JC', 'TC', '9C', '8C', '7C']
        actual = poker.straight(sf)
        expected = True
        self.assertEqual(actual, expected)

        fk = ['5S', '5H', '5D', '5C', 'KS']
        actual2 = poker.straight(fk)
        expected2 = False
        self.assertEqual(actual2, expected2)





if __name__ == '__main__':
    unittest.main(exit=False)