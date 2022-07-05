import unittest

from Solver import findWords

class TestSolver(unittest.TestCase):
    def test_findWords(self):
        letter='Ε'
        color='G'
        position=0
        words=['ΕΝΑ','ΔΥΟ','ΤΡΙΑ','ΤΕΣΣΕΡΑ']
        wordList=[]
        testCase=findWords(letter,color,position,words,wordList)

        self.assertEqual(['ΕΝΑ',testCase])


        letter='Δ'
        color='G'
        position=0
        words=['ΕΝΑ','ΔΥΟ','ΤΡΙΑ','ΤΕΣΣΕΡΑ']
        wordList=[]
        testCase=findWords(letter,color,position,words,wordList)

        self.assertNotEqual(['ΕΝΑ',testCase])
        
        letter='E' #  E : Latin Letter
        color='G'
        position=0
        words=['ΕΝΑ','ΔΥΟ','ΤΡΙΑ','ΤΕΣΣΕΡΑ']
        wordList=[]
        testCase=findWords(letter,color,position,words,wordList)
        self.assertNotEqual(['ΕΝΑ',testCase])
        
    
        
        letter='Ε'
        color='Y'  #  Greek Char
        position=2
        words=['ΕΝΑ','ΔΥΟ','ΤΡΙΑ','ΤΕΣΣΕΡΑ']
        wordList=[]
        testCase=findWords(letter,color,position,words,wordList)
        self.assertNotEqual(['ΕΝΑ',testCase])
        
        
        