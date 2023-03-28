import inc_dec
import unittest


class Test_TestIncDec(unittest.TestCase):
    def test_inc(self):
        self.assertEqual(inc_dec.increment(3), 4)
        
    def test_dec(self):
        self.assertEqual(inc_dec.decrement(3), 2)
        

if __name__ == '__main__':
    unittest.main()
    
