import unittest

import contfrac_addchain as ac

class test_continued_fraction(unittest.TestCase):
    
    #this is example 9.37 in Doche Chapter 9 p.162
    def test_chain_1(self):
        n = 87 
        k = ac.alpha(n)
        result = ac.chain(n,k)
        known = [1,2,3,6,7,10,20,40,80,87]
        self.assertEqual(result, known)
        
    #Since addition chains are not unique, how can we verify it? Ask Riad
    def test_chain_2(self):
        n = 29
        k = ac.alpha(n)
        result = ac.chain(n,k)
        known = [1, 2, 4, 8, 9, 17, 25, 29]
        self.assertEqual(len(result), len(known))
        

if __name__ == "__main__":
    unittest.main()

        