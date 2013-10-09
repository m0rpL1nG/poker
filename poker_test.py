import unittest
import poker
class Testpoker(unittest.TestCase):
    '''Example unittest test methods for poker. [Return the hand rank of a hand]
    '''
    def test_poker(self):
        """

        Test poker function with straight flush and straight flush hands

        ['JC', 'TC', '9C', '8C', '7C'] and ['JS', 'TS', '9S', '8S', '7S']

        """
        sf = ['JC', 'TC', '9C', '8C', '7C']
        sf2 = ['JS', 'TS', '9S', '8S', '7S']
        actual = poker.poker([sf, sf2])
        expected = [['JC', 'TC', '9C', '8C', '7C'], ['JS', 'TS', '9S', '8S', '7S']]
        self.assertEqual(actual,expected)

    def test_poker_2(self):
        """

        Test poker function with straight flush and four of a kind hands

        ['JC', 'TC', '9C', '8C', '7C'] and ['5S', '5H', '5D', '5C', 'KS']

        """
        sf = ['JC', 'TC', '9C', '8C', '7C']
        fk = ['5S', '5H', '5D', '5C', 'KS']
        actual = poker.poker([sf, fk])
        expected = [['JC', 'TC', '9C', '8C', '7C']]
        self.assertEqual(actual,expected)

        

    def test_poker_3(self):
        """

        Test poker function with one pair and two pair hands

        ['5S', '3H', '9D', '8C', '8S'] and ['5S', '5H', '9D', '8C', '8S']

        """
        op = ['5S', '3H', '9D', '8C', '8S']
        tp = ['4S', '4H', '7D', '3C', '3S']
        actual = poker.poker([op, tp])
        print '$$$$$$$$$$$$$',poker.poker([op, tp])
        expected = [['4S', '4H', '7D', '3C', '3S']]
        self.assertEqual(actual,expected)



    def test_hand_rank(self):
        """Test hand_rank with straight flush hand 

        ['JC', 'TC', '9C', '8C', '7C']
        """
        sf = ['JC', 'TC', '9C', '8C', '7C']
        actual = poker.hand_rank(sf)
        expected = 8,10
        self.assertEqual(actual, expected)


    def test_hand_rank_2(self):
        """
        Test hand_rank with four of a kind hand

        ['6H', '6S', '6D', '6C', 'KS']
        """
        fk = ['6H', '6S', '6D', '6C', 'KS']
        actual = poker.hand_rank(fk)
        expected = 7,6
        self.assertEqual(actual, expected)

  
    def test_straight_flush(self):
        """
        Test straight flush with straight flush hand
        ['6H', 'TH', '9H', '7H', '8H']
        """
        sf = ['6H', 'TH', '9H', '7H', '8H']
        actual = poker.straight_flush(sf)
        expected = True,9
        self.assertEqual(actual,expected)

    def test_straight_flush_2(self):
        """
        Test straight flush with straight hand
        ['6C', 'TH', '9D', '7D', '8C']
        """
        st = ['6C', 'TH', '9D', '7D', '8C']
        actual = poker.straight_flush(st)
        expected = False,0
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


    def test_straight(self):
        """
        Test straight with straight hand

        ['4H', '5S', '3D', '6C', '7S']
        """
        st = ['4H', '5S', '3D', '6C', '7S']
        actual = poker.straight(st)
        expected = True,6
        self.assertEqual(actual,expected)


    def test_straight_2(self):
        """
        Test straight with four of a kind hand

        ['6H', '6S', '6D', '6C', 'KS']
        """
        fk = ['6H', '6S', '6D', '6C', 'KS']
        actual = poker.straight(fk)
        expected = False,0
        self.assertEqual(actual,expected)

    def test_onepair(self):
        """
        Test onepair with onepair hand

        ['4H', '5S', '3D', '6C', '7S']
        """
        op = ['5S', '3H', '9D', '8C', '8S']
        actual = poker.kind(op, 2)
        expected = 8
        self.assertEqual(actual,expected)

    def test_onepair_2(self):
        """
        Test onepair with straight hand

        ['5S', '3H', '9D', '7C', '8S']
        """
        st = ['5S', '3H', '9D', '7C', '8S']
        actual = poker.kind(st, 2)
        expected = 0
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


    def test_allmax(self):
        """
        Test test_allmax with straight flush and straight flush hands

        ['JC', 'TC', '9C', '8C', '7C'] and ['JS', 'TS', '9S', '8S', '7S']
        """
        sf = ['JC', 'TC', '9C', '8C', '7C']
        sf2 = ['JS', 'TS', '9S', '8S', '7S']
        actual = poker.allmax([sf, sf2])
        expected = [['JC', 'TC', '9C', '8C', '7C'], ['JS', 'TS', '9S', '8S', '7S']]
        self.assertEqual(actual,expected)


    def test_kind(self):
        """
        Test kind n = 3 with three of a kind hand

        ['QS', 'QC', 'QD', '4H', '5H']
        """
        tk = ['QS', 'QC', 'QD', '4H', '5H']
        actual = poker.kind(tk,3)
        expected = 12
        self.assertEqual(actual,expected)


    def test_kind_2(self):
        """
        Test kind n = 3 with three of a kind hand

        ['6H', '6S', '6D', '7C', 'KS']
        """
        tk = ['6H', '6S', '6D', '7C', 'KS']
        actual = poker.kind(tk,3)
        expected = 6
        self.assertEqual(actual,expected)


    def test_kind_3(self):
        """
        Test kind n = 3 with four of a kind hand

        ['6H', '6S', '6D', '6C', 'KS']
        """
        fk = ['6H', '6S', '6D', '6C', 'KS']
        actual = poker.kind(fk,3)
        expected = 0
        self.assertEqual(actual,expected)


    def test_kind_4(self):
        """
        Test kind n = 4 with four of a kind hand

        ['6H', '6S', '6D', '6C', 'KS']
        """
        fk = ['6H', '6S', '6D', '6C', 'KS']
        actual = poker.kind(fk,4)
        expected = 6
        self.assertEqual(actual,expected)


    def test_kind_5(self):
        """
        Test kind n = 4 with three of a kind hand

        ['6H', '6S', '6D', '7C', 'KS']
        """
        thk = ['6H', '6S', '6D', '7C', 'KS']
        actual = poker.kind(thk,4)
        expected = 0
        self.assertEqual(actual,expected)



    def test_kind_6(self):
        """
        Test kind full house hand with full house hand

        ['5H', '5S', '5D', '8C', '8S']
        """
        fh = ['5H', '5S', '5D', '8C', '8S']
        actual = poker.kind(fh,3) and poker.kind(fh,2)
        expected = 8
        self.assertEqual(actual,expected)


    def test_kind_7(self):
        """
        Test kind full house hand with four of a kind hand

        ['6H', '6S', '6D', '6C', 'KS']
        """
        fk = ['6H', '6S', '6D', '6C', 'KS']
        actual = poker.kind(fk,3) and poker.kind(fk,2)
        expected = False
        self.assertEqual(actual,expected)
        

if __name__ == '__main__':
    unittest.main(exit=False)
