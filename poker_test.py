import unittest
import poker
class Testpoker(unittest.TestCase):
    '''Example unittest test methods for poker. [Return the hand rank of a hand]
    '''
    def test_poker(self):
        """Test poker with straight flush hand

        ['JC', 'TC', '9C', '8C', '7C']
        """
        sf = ['JC', 'TC', '9C', '8C', '7C']
        actual = poker.poker(sf)
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
    
    def test_straight_flush(self):
        """
        Test straight flush with straight flush hand
        ['6H', 'TH', '9H', '7H', '8H']
        """
        sf = ['6H', 'TH', '9H', '7H', '8H']
        actual = poker.straight_flush(sf)
        expected = True
        self.assertEqual(actual,expected)

    def test_straight_flush_2(self):
        """
        Test straight flush with straight hand
        ['6C', 'TH', '9D', '7D', '8C']
        """
        st = ['6C', 'TH', '9D', '7D', '8C']
        actual = poker.straight_flush(st)
        expected = False
        self.assertEqual(actual,expected)
        
    def test_flush(self):
        """
        Test flush with flush hand
        ['JC', 'TC', '9C', '8C', '7C']
        """
        fl = ['JC', 'TC', '9C', '8C', '7C']
        actual = poker.flush(fl)
        expected = True
        self.assertEqual(actual,expected)

        
    def test_flush_2(self):
        """
        Test flush with straight hand
        ['3C', '4S', '5D', '6C', '7S']
        """
        st = ['3C', '4S', '5D', '6C', '7S']
        actual = poker.flush(st)
        expected = False
        self.assertEqual(actual,expected)


    def test_full_house(self):
        """
        Test full_house with full house hand

        ['5H', '5S', '5D', '8C', '8S']
        """
        fh = ['5H', '5S', '5D', '8C', '8S']
        actual = poker.full_house(fh)
        expected = True
        self.assertEqual(actual,expected)


    def test_full_house_2(self):
        """
        Test full_house with four of a kind hand

        ['6H', '6S', '6D', '6C', 'KS']
        """
        fk = ['6H', '6S', '6D', '6C', 'KS']
        actual = poker.full_house(fk)
        expected = False
        self.assertEqual(actual,expected)
        
    def test_straight(self):
        """
        Test straight with straight hand

        ['4H', '5S', '3D', '6C', '7S']
        """
        st = ['4H', '5S', '3D', '6C', '7S']
        actual = poker.straight(st)
        expected = True
        self.assertEqual(actual,expected)


    def test_straight_2(self):
        """
        Test straight with four of a kind hand

        ['6H', '6S', '6D', '6C', 'KS']
        """
        fk = ['6H', '6S', '6D', '6C', 'KS']
        actual = poker.straight(fk)
        expected = False
        self.assertEqual(actual,expected)

    def test_onepair(self):
        """
        Test onepair with onepair hand

        ['4H', '5S', '3D', '6C', '7S']
        """
        op = ['5S', '3H', '9D', '8C', '8S']
        actual = poker.onepair(op)
        expected = True
        self.assertEqual(actual,expected)

    def test_onepair_2(self):
        """
        Test onepair with straight hand

        ['5S', '3H', '9D', '7C', '8S']
        """
        st = ['5S', '3H', '9D', '7C', '8S']
        actual = poker.onepair(st)
        expected = False
        self.assertEqual(actual,expected)


    def test_twopair(self):
        """
        Test twopair with twopair hand

        ['5S', '5H', '9D', '8C', '8S']
        """
        tp = ['5S', '5H', '9D', '8C', '8S']
        actual = poker.twopair(tp)
        expected = True
        self.assertEqual(actual,expected)

    def test_twopair_2(self):
        """
        Test twopair with straight hand

        ['4H', '5S', '3D', '6C', '7S']
        """
        st = ['4H', '5S', '3D', '6C', '7S']
        actual = poker.twopair(st)
        expected = False
        self.assertEqual(actual,expected)



if __name__ == '__main__':
    unittest.main(exit=False)