import unittest
import poker
class Testpoker(unittest.TestCase):
    """unittest test methods for poker. [Return the hand rank of a hand]"""
    def test_poker(self):
    	"""Test poker with straight flush hand

        ['JC', 'TC', '9C', '8C', '7C']
        """
    	sf = ['JC', 'TC', '9C', '8C', '7C']
    	actual = poker.poker([sf])
        expected = 8
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(exit=False)