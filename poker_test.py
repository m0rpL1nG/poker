import unittest
import poker
class Testpoker(unittest.TestCase):
    '''Example unittest test methods for poker. [Return the hand rank of a hand]'''
    def test_poker(self):
    	"""Test poker with straight flush hand

        ['JC', 'TC', '9C', '8C', '7C']
        """
    	sf = ['JC', 'TC', '9C', '8C', '7C']
    	actual = poker.poker([sf])
        expected = 8
        self.assertEqual(actual, expected)


    def test_hand_rank(self):
        """Test hand_rank with straight flush hand 

        ['JC', 'TC', '9C', '8C', '7C']
        """
        sf = ['JC', 'TC', '9C', '8C', '7C']
        actual = poker.hand_rank(sf)
        expected = 8
        self.assertEqual(actual, expected)


    def test_hand_rank_2(self):
        """
        Test hand_rank with four of a kind hand

        ['6H', '6S', '6D', '6C', 'KS']
        """
        fk = ['6H', '6S', '6D', '6C', 'KS']
        actual = poker.hand_rank(fk)
        expected = 7
        self.assertEqual(actual, expected)


    def test_four_of_a_kind(self):
        """
        Test four_of_a_kind with four of a kind hand

        ['6H', '6S', '6D', '6C', 'KS']
        """
        fk = ['6H', '6S', '6D', '6C', 'KS']
        actual = poker.four_of_a_kind(fk)
        expected = True
        self.assertEqual(actual,expected)


    def test_four_of_a_kind_2(self):
        """
        Test four_of_a_kind with three of a kind hand

        ['6H', '6S', '6D', '7C', 'KS']
        """
        thk = ['6H', '6S', '6D', '7C', 'KS']
        actual = poker.four_of_a_kind(thk)
        expected = False
        self.assertEqual(actual,expected)



if __name__ == '__main__':
    unittest.main(exit=False)