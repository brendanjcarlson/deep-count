import unittest
from whiteboard import solution

class WhiteboardTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution([]), 0)
    
    def test_2(self):
        self.assertEqual(solution([1, 2, 3]), 3)

    def test_3(self):
        self.assertEqual(solution(['a', 'b', 'c', ['d']]), 5)

    def test_4(self):
        self.assertEqual(solution([1, 2, [3, 4, [5]]]), 7) 


if __name__ == "__main__":
    unittest.main()


