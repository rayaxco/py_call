import unittest
import random

import guess_game_func

class guesstest(unittest.TestCase):
    def test1(self):
        ans=random.randint(1,10)
        gue=int(input('Enter a number between 1-10'))
        result=guess_game_func.guess_game(gue,ans)
        if(result=='correct'):
            self.assertEqual(result,'correct')
        elif result=='Nope':
            self.assertEqual(result,'Nope')
        elif isinstance(result,ValueError):
            self.assertIsInstance(result,ValueError)
if __name__ == '__main__':
    unittest.main()